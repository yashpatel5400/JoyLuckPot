from flask import Flask
app = Flask(__name__)

@app.route("/")
def Hello():
    return "Hello World!"

@app.route("/next")
def next():
	return "Next World!"

@app.route('/user/<name>') 
def user_profile(name):
	#show name of user
	return 'User %s' % name

if __name__ == "__main__":
    app.run()