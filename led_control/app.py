import RPi.GPIO as GPIO
from flask import Flask, render_template
state = 'off'
app=Flask(__name__)
def led_on_off(onoff):
	if onoff == 'on':
		GPIO.output(21,0)
	elif onoff == 'off':
		GPIO.output(21,1)
@app.route('/') 
def index():
	return render_template('index.html', state=state)

@app.route('/led/<onoff>') 
def led(onoff):
	global state
	state = onoff
	led_on_off(state)
	print('led %s' %state)
	return render_template('index.html', state = onoff)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
led_on_off('off')
if __name__=='__main__':
	app.run(host='192.168.0.160', port=8888, debug=True)
	GPIO.cleanup()