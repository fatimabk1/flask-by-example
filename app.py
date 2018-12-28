from flask import Flask, url_for, request
app = Flask(__name__)

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