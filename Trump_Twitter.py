# Jason D. Miller
# github.com/hack-r

from twython import TwythonStreamer
import RPi.GPIO as GPIO
import time

C_KEY =  ""
C_SECRET = ""
A_TOKEN = "-"
A_SECRET = ""

def blink():
     GPIO.setmode(GPIO.BOARD)
     GPIO.setup(18,GPIO.OUT)
     GPIO.output(18, GPIO.HIGH)
     time.sleep(1)
     GPIO.output(18, GPIO.LOW)

class MyStreamer(TwythonStreamer):
     def on_success(self, data):
         if 'text' in data:
              blink()
              print("Got it.")

stream = MyStreamer(C_KEY, C_SECRET, A_TOKEN, A_SECRET)

stream.statuses.filter(track="Trump")







