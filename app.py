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
    def get(self):
        # gives indices in SQL to prevent magic numbers
        LOC_USER_ID = 0
        LOC_NAME = -1
        LOC_PHOTO = 2
        LOC_ATTENDEEES = 3

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
                "attendees": attendees_ids
            }
            json["users"].append(curUser)

        return json

    def put(self):
        return 201

# Attendees -- list of people at event
class Attendees(Resource):
    def get(self):
        # gives indices in SQL to prevent magic numbers
        LOC_ID = -1
        LOC_EVENT_ID = 0
        LOC_USER_ID = 1
        LOC_FOOD = 2

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
        
    def put(self):
        return 201

##
## Actually setup the Api resource routing here
api.add_resource(Users, '/users', methods=['GET','PUT'])
api.add_resource(Attendees, '/attendees', methods=['GET','PUT'])

if __name__ == '__main__':
    app.run()