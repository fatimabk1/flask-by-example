# import os to access environmental variables
import os
from flask import Flask, url_for, request
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)

# import app_settings from .env file via os
app.config.from_objects(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = FALSE

# initatite db connection
db = SQLAlchemy(app)

# importing class Result from models.py
from models import Result


@app.route('/')
def index():
	return "<h1>Hello World!<h1>"

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('templates/hello.html', name=name)

@app.route('/bio/')
def bio():
	return "You've reached the bio page!"

@app.route('/<string:username>')
def user(username):
	return 'User {}'.format(username)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return user('POST')
    else:
        return user('GET')

if __name__=='__main__':
	app.run()