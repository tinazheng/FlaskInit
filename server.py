from flask import *
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/61a')
def python():
	return "Python is awesome"

if __name__ == '__main__':
    app.run(debug=True)