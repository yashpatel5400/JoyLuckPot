import sqlite3
connection_events = sqlite3.connect("events.db")
connection_food = sqlite3.connect("food.db")
connection_users = sqlite3.connect("users.db")

cursor_events = connection_events.cursor()
cursor_food = connection_food.cursor()
cursor_users = connection_users.cursor()

sql_command_events = """
CREATE TABLE [Events] (
    [EventID]  INT NOT NULL,
    [Longitude] FLOAT NOT NULL,
    [Host]     VARCHAR (255) NOT NULL, 
    [Time] TIME NOT NULL, 
    [PotLuck] INT NOT NULL, 
    [Private] INT NOT NULL, 
    [Latitude] FLOAT NOT NULL, 
    [maxGuests] INT NOT NULL, 
    [currentGuests] INT NOT NULL, 
    CONSTRAINT [PK_Events] PRIMARY KEY ([EventID])
);
"""

sql_command_food = """
CREATE TABLE [Food] (
    [EventID]      INT NOT NULL,
    [UserID]      INT NOT NULL,
    [Food] VARCHAR (255) NULL
);
"""

sql_command_users = """
CREATE TABLE [Users] (
    [UserID] VARCHAR (255) NOT NULL,
    [Password] VARCHAR (255) NOT NULL,
    [Specialities] VARCHAR(255) NOT NULL, 
    [Address] VARCHAR(255) NOT NULL, 
    [Preferences] VARCHAR(255) NOT NULL, 
    [Picture] VARCHAR(255),
    CONSTRAINT [PK_Users] PRIMARY KEY ([UserID])
);
"""


# Create tables -- commented as already made
# cursor_events.execute(sql_command_events)
# cursor_food.execute(sql_command_food)
# cursor_users.execute(sql_command_users)
