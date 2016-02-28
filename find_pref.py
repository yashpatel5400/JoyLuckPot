import wikipedia
import wolframalpha
import pymssql

conn = pymssql.connect(server='daphney.database.windows.net', 
	user='daphne@daphney', password='Princeton2018', database='Profiles')
cur = conn.cursor()

# Person's specialities
specialities = ["Chocolate Cake", "Kimchi", "Sauce"]

# Bunch of people's preferences
pref_1 = ["Korean", "Pie", "Cake"]
pref_2 = ["Dessert", "Cheese", "Sweet"]
pref_3 = ["Indian", "Spicy", "Dessert"]

# What's already being brought to the event
brought = ["Cheesecake", "Chips and Spicy Salsa"]
# ------------------------------------------------
# Returns recommendations for what to cook (array)
def get_prefs(event):
	prefs = [pref_1, pref_2, pref_3]
	final_prefs = []
	for pref in prefs:
		pref = [s.lower() for s in pref]
		final_prefs += pref 

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

# given recommendations, determines all their corresponding recipes
def get_recipes(recommendations):
	client = wolframalpha.Client("7G2PKA-T85X7T866X")
	for option in best_options:
		res = client.query('{}'.format(best_options[0]))
		for pod in res.pods:
			print(next(res.results).text)