import RPi.GPIO as GPIO
from flask import Flask, render_template
state = 'off'
app=Flask(__name__)
def led_on_off(onoff):
  if onoff == 'forward':
    GPIO.output(19,1)
    GPIO.output(16,0)
    GPIO.output(18,1)
    GPIO.output(17,0)

  elif onoff == 'backward':
    GPIO.output(19,0)
    GPIO.output(16,1)
    GPIO.output(18,0)
    GPIO.output(17,1)
 
  elif onoff == 'left':
    GPIO.output(19,1)
    GPIO.output(16,0)
    GPIO.output(18,0)
    GPIO.output(17,0)
 
  elif onoff == 'right':
    GPIO.output(19,0)
    GPIO.output(16,0)
    GPIO.output(18,1)
    GPIO.output(17,0)
  elif onoff == 'off':
    GPIO.output(19,0)
    GPIO.output(16,0)
    GPIO.output(18,0)
    GPIO.output(17,0)

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
 GPIO.setup(19, GPIO.OUT)
 GPIO.setup(16, GPIO.OUT)
 GPIO.setup(18, GPIO.OUT)
 GPIO.setup(17, GPIO.OUT)
 led_on_off('off')
if __name__=='__main__':
  app.run(host='192.168.0.11', port=8888, debug=True)
  GPIO.cleanup()
