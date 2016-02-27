from flask import Flask, url_for
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

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/projects/')
def projects():
    return 'The project page'

#@app.route('/login')
#def login(): pass

#with app.test_request_context():
#	print url_for('login')

@app.route('/home')
def home():
	return render_template('login.html')

if __name__ == "__main__":
    app.run()