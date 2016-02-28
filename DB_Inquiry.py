import sqlite3
import pandas as pd

connection_events = sqlite3.connect("events.db")
connection_food = sqlite3.connect("food.db")
connection_users = sqlite3.connect("users.db")

cursor_events = connection_events.cursor()
cursor_food = connection_food.cursor()
cursor_users = connection_users.cursor()

SQL_make_users_1 = """
	INSERT INTO [Users]
	VALUES ("user_1", "pass_1", "Apple Pie, Kimchi, Cornbread, Pizza", 
		"Test Road", "Italian, Spicy, Korean", "");
"""

SQL_make_users_2 = """
	INSERT INTO [Users]
	VALUES ("user_2", "pass_2", "Sushi, Seafood, Bread, Toast", 
		"Test Road 2", "Indian, Dessert, Pie", "");
"""

SQL_make_users_3 = """
	INSERT INTO [Users]
	VALUES ("user_3", "pass_3", "Cake, Palak Paneer, Jambalaya", 
		"Test Road 3", "Japanese, Bread, Grains", "");
"""

SQL_make_food_1 = """
	INSERT INTO [Food]
	VALUES (829982, 234278, "Banana Pie");
	"""

SQL_make_food_2 = """
	INSERT INTO [Food]
	VALUES (829982, 234238, "Cake");
"""

SQL_make_events = """
	INSERT INTO [Events]
	VALUES (829982, 23.4328, "John", 1997-07-16, 1, 0, 43.2341, 10, 5)
"""

SQL_read_query = """
	SELECT * from [Food]
"""

cursor_users.execute(SQL_make_users_1)
cursor_users.execute(SQL_make_users_2)
cursor_users.execute(SQL_make_users_3)

cursor_events.execute(SQL_make_events)

cursor_food.execute(SQL_make_food_1)
cursor_food.execute(SQL_make_food_2)