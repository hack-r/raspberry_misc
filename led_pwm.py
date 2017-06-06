import RPi.GPIO as GPIO
import time

GPIO.cleanup()

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT) #set pin 18 to output

p = GPIO.PWM(18,50)        #set the PWM on pin 18 to 50%
p.start(50) 

while True: # purposely infinite loop
    for i in range (100):
        p.ChangeDutyCycle(i)
        time.sleep(0.02)         #These last three lines are going to loop and increase the power from 1% to 100% gradually
    for i in range(100):
        p.ChangeDutyCycle(100-i)
	time.sleep(0.02)         #These three lines loop and decrease the power from 100%-1% gradually

