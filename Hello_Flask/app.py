#hello_flask.py
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
	return "Hello RasberryPi with flask')

if __name__ == '__main__':
	app.run(debug=True, host='192.168.0.11', port=8888)