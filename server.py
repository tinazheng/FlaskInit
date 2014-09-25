from flask import *
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

def question(number):
	if number == 1:
		return "What is the best programming langauge?"
	if number == 2:
		return "Fill in the blank: John _____"

@app.route('/quiz/<int:num>')
def game(num):
	s = question(num)
	return render_template("game.html", question=s, level=num)

@app.route('/quiz/<int:num>', methods=['POST'])
def check(num):
	answer = request.form['text']
	if num == 1:
		if answer == "Python":
			return redirect('/quiz/'+str(num+1))
	if num == 2:
		if answer == "DeNero":
			return redirect('/quiz/' + str(num-1))
		else:
			return "Wrong"

if __name__ == '__main__':
    app.run(debug=True)