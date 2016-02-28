from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import pymssql
import json

app = Flask(__name__)
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
            curID = result[LOC_USER_ID]
            
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
                "name": results[LOC_NAME],
                "photo": results[LOC_PHOTO],
                "attendees": attendees_ids,
                "specialties": results[LOC_SPECIALTIES],
                "preferences": results[LOC_PREFERENCES]
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
        results_parsed = []
        while results:
            results_parsed.append(results)
            results = cur.fetchone()
            curUser = {
                "id": results[LOC_ID],
                "user": results[LOC_USER_ID],
                "event": results[LOC_EVENT_ID],
                "food": results[LOC_FOOD]
            }
            json["users"].append(curUser)

        return json
        
    def put(self, update):
        LOC_EVENT_ID
        LOC_USER_ID
        LOC_FOOD
        LOC_ID

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

##
## Actually setup the Api resource routing here
api.add_resource(Users, '/users', methods=['GET','PUT'])
api.add_resource(Attendees, '/attendees', methods=['GET','PUT'])

if __name__ == '__main__':
    app.run()