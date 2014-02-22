# import RPi.GPIO as GPIO
from lib.Adafruit_PWM_Servo_Driver import PWM
import time

channels = [0 for i in range(16)]

# Initialise the PWM device using the default address
pwm = PWM(0x40, debug=True)
pwm.setPWMFreq(60)                        # Set frequency to 60 Hz

# Initialise the GPIO output channels
# GPIO.setmode(GPIO.BCM)
# RED = 21
# GREEN = 17
# GPIO.setup(RED, GPIO.OUT)
# GPIO.setup(GREEN, GPIO.OUT)
# GPIO.output(RED,False)
# GPIO.output(GREEN,False)

def setChannel(channel,val):
    channel = int(channel)
    val = int(val)
    channels[channel] = val
    pwm.setPWM(channel, 0, val*16)

def getState():
    return {'channels':channels}

