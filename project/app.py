from flask import Flask, render_template, url_for

app = Flask(__name__)
@app.route('/')
def hello():
	return render_template('save.html')


@app.route('/next')
def next():
	return render_template('next.html')

@app.route('/third')
def third():
	return render_template('third.html')

if __name__ == '__main__':
	app.run(debug=True)

 