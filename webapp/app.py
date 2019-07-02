from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
??? return render_template('index.html')
@app.route('/cakes')
def cakes():
??? return 'Yummy cakes!'
@app.route('/hello/<_name>')
def hello(_name):
??? return render_template('page.html', name=_name)
def cakes():
??? return 'Yummy cakes!'

if __name__ == '__main__':
??? app.run(debug=True, host='192.168.0.11:8888')