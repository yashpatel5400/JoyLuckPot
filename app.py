from flask import Flask, send_file
from flask_restful import reqparse, abort, Api, Resource
import pymssql
import json

app = Flask(__name__, static_folder="dist", static_url_path="")
api = Api(app)
conn = pymssql.connect(server='daphney.database.windows.net',
    user='daphne@daphney', password='Princeton2018', database='Profiles')
cur = conn.cursor()

# User -- person attending event
class Users(Resource):
    LOC_USER_ID = 0
    LOC_PHOTO = 1
    LOC_SPECIALTIES = 2
    LOC_PREFERENCES = 3
    LOC_NAME = 4

    def get(self):
        # gives indices in SQL to prevent magic numbers
        json = {"users": []}
        SQL_command = "SELECT * FROM Users"
        cur.execute(SQL_command)

        results = cur.fetchone()
        results_parsed = []
        while results:
            results_parsed.append(results)
            results = cur.fetchone()

        for result in results_parsed:
            curID = result[self.LOC_USER_ID]

            SQL_command_2 = "SELECT FoodComboID FROM Food \
                WHERE UserID = {}".format(curID)
            cur.execute(SQL_command_2)

            results_2 = cur.fetchone()
            attendees_ids = []
            while results_2:
                attendees_ids.append(results_2[0])
                results_2 = cur.fetchone()

            curUser = {
                "id": curID,
                "name": result[self.LOC_NAME],
                "photo": result[self.LOC_PHOTO],
                "attendees": attendees_ids,
                "specialties": result[self.LOC_SPECIALTIES],
                "preferences": result[self.LOC_PREFERENCES]
            }
            json["users"].append(curUser)

        return json

    def put(self, update):
        new_user = update["users"][0]
        new_user_id = new_user['id']
        new_user_photo = new_user['photo']
        new_user_specialties = new_user['specialties']
        new_user_preferences = new_user['preferences']
        new_user_name = new_user['name']

        SQL_command_new = " INSERT INTO Users\
            VALUES ({},{},{},{},{})".format(new_user_id, new_user_photo,
            new_user_specialties, new_user_preferences, new_user_name)
        cur.execute(SQL_command_new)

# Attendees -- list of people at event
class Attendees(Resource):
    # gives indices in SQL to prevent magic numbers
    LOC_EVENT_ID = 0
    LOC_USER_ID = 1
    LOC_FOOD = 2
    LOC_ID = 3

    def get(self):
        json = {"attendees": []}
        SQL_command = "SELECT * FROM Food"
        cur.execute(SQL_command)

        results = cur.fetchone()
        while results:
            curUser = {
                "id": results[self.LOC_ID],
                "user": results[self.LOC_USER_ID],
                "event": results[self.LOC_EVENT_ID],
                "food": results[self.LOC_FOOD]
            }
            json["attendees"].append(curUser)
            results = cur.fetchone()

        return json

    def put(self, update):
        new_attendees = update["attendees"][0]
        new_attendees_event = new_attendees['event']
        new_attendees_user = new_attendees['user']
        new_attendees_food = new_attendees['food']
        new_attendees_id = new_attendees['id']

        SQL_command_new = " INSERT INTO Food\
            VALUES ({},{},{},{})".format(new_attendees_event,
                new_attendees_user, new_attendees_food,
                new_attendees_id)
        cur.execute(SQL_command_new)

class Events(Resource):
    LOC_ID = 0
    LOC_LNG = 1
    LOC_HOST = 2
    LOC_TIME = 3
    LOC_POTLUCK = 4
    LOC_PRIVATE = 5
    LOC_LAT = 6
    LOC_MAXGUESTS = 7
    LOC_CURGUESTS = 8
    LOC_TITLE = 9
    LOC_DESC = 10

    def get(self):
        json = {"events": []}
        cur.execute("SELECT * FROM Events")

        results = cur.fetchone()
        while results:
            json["events"].append({
                "id": results[self.LOC_ID],
                "title": results[self.LOC_TITLE],
                "description": results[self.LOC_DESC],
                "time": results[self.LOC_TIME].isoformat(),
                "lat": results[self.LOC_LAT],
                "lng": results[self.LOC_LNG]
            })
            results = cur.fetchone()

        return json

##
## Actually setup the Api resource routing here
api.add_resource(Users, '/users', methods=['GET','PUT'])
api.add_resource(Attendees, '/attendees', methods=['GET','PUT'])
api.add_resource(Events, '/events', methods=['GET'])


@app.route('/')
def index():
  return send_file('dist/index.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
