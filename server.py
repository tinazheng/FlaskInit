from flask import *
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/quiz')
def game():
	return render_template("game.html")

if __name__ == '__main__':
    app.run(debug=True)