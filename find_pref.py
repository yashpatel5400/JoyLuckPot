import wikipedia
import wolframalpha
import pymssql
import google
import re

conn = pymssql.connect(server='daphney.database.windows.net',
    user='daphne@daphney', password='Princeton2018', database='Profiles')
cur = conn.cursor()

# returns IDs of users and food who attended event
# as an array of arrays of [[IDs],[Food]]
def get_user_food(event):
    SQL_query = "SELECT UserID, Food FROM Food \
        WHERE EventID = {}".format(event)
    cur.execute(SQL_query)
    results = cur.fetchone()
    ids_parsed = []
    food_parsed = []
    while results:
        ids_parsed.append(results[0])
        food_parsed.append(results[1])
        results = cur.fetchone()

    return [ids_parsed, food_parsed]

def get_prefs(users):
    full_prefs = []
    for user in users:
        SQL_query = "SELECT Preferences FROM Users WHERE UserID = {}".format(user)
        cur.execute(SQL_query)
        results = cur.fetchone()
        preferences = []
        while results:
            preferences.append(results[0])
            results = cur.fetchone()
        full_prefs.append(preferences)
    return full_prefs

# returns array of the specialities of user
def get_specialities(user):
    SQL_query = "SELECT Specialities FROM Users \
        WHERE UserID = {}".format(user)
    cur.execute(SQL_query)
    specialities = cur.fetchone()[0].split(', ')
    return specialities

# Get recipe link
def get_recipe(food):
    query = "{} Recipe".format(food)
    results = google.search(query, stop=1)
    return (list(results)[0])

# Returns recommendations for what to cook (array)
# for a given person with userID in the form of
# [[item1, item2], [item1 recipe, item2 recipe], 
# [[pics of item1], [pics of item2]]]
def get_recs(event, userID):
    overall_values = get_user_food(event)
    specialities = get_specialities(userID)
    users = overall_values[0]

    # What's already being brought to the event
    brought = overall_values[1]

    # People's preferences who are attending event
    prefs = get_prefs(users)

    final_prefs = []
    for pref in prefs:
        cur_pref = pref[0].replace(',', '').split()
        cur_pref = [s.lower() for s in cur_pref]
        final_prefs += cur_pref

    # removes repeats
    final_prefs = list(set(final_prefs))

    # lookup pages with scraper for each of the x=
    pages = [wikipedia.page(speciality) for speciality in specialities]

    # bunch of unintelligible code to change from binary to str
    description = {}
    for speciality in specialities:
        description[speciality] = [word.decode('utf-8').encode('cp850','replace').decode('cp850').lower()
            for word in wikipedia.page(speciality).summary.encode("utf-8").split()]

    # all the descriptors put into single list
    values = []
    for desc in list(description.values()):
        values += desc
    values = list(set(values))

    # determine if any overlap between specialities and preferences
    best_options = []
    mid_options = []
    for pref in final_prefs:
        # determines if people like this speciality
        if pref in values:
            # determines which speciality people like
            for speciality in description:
                if pref in description[speciality]:
                    final_spec = speciality

            # case where someone already brought
            if final_spec in brought:
                mid_options.append(final_spec)

            # case where no one has brought dish already
            else:
                best_options.append(final_spec)

    urls = [get_recipe(food) for food in best_options]
    images = []

    CUTOFF = 2
    for option in best_options:
        page = wikipedia.page(option)
        length = len(page.images)
        if length > CUTOFF:
            images.append(page.images[:CUTOFF])
        else:
            images.append(page.images)
    return [best_options, urls, images]

# given recommendations, returns nutrition facts
# as a dictionary
def get_nutrition_fact(recommendations):
    client = wolframalpha.Client("7G2PKA-T85X7T866X")
    for option in recommendations:
        res = client.query('{}'.format(option))

        # determines where the nutrition facts are
        for pod in res.pods:
            if "total fat" in pod.text:
                final_text = pod.text
                break

        # reformats the nutrion facts into dictionary
        parsed_text = final_text.strip().split('\n')
        simplified_text = []
        for line in parsed_text:
            cut_index = line.find('|')
            if cut_index != -1:
                simplified_text.append(" ".join(line[:cut_index].split()))
        
        nutrition_facts = {}
        for line in simplified_text:
            num_index = re.search("\d", line)
            if num_index:
                key = line[:num_index.start()]
                val = line[num_index.start():]
                nutrition_facts[key] = val
        return nutrition_facts

# Testing purpose
# if __name__ == "__main__":
    # sample_recs = get_recs(3, 2)
    # print(sample_recs)
    # get_nutrition_fact(['Lo Mein'])