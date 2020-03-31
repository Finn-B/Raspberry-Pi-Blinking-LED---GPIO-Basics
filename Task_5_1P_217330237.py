import RPi.GPIO as GPIO
import time

# USE GPIO NUMBERS NOT PIN NUMBERS
GPIO.setmode(GPIO.BCM)

#PIN DEFINITION
led = 18

#GPIO SETUP
GPIO.setup(led, GPIO.OUT)
GPIO.output(led, GPIO.LOW)


#MAIN LOOP
try:
    
    while 1:
        GPIO.output(led, GPIO.HIGH)
        time.sleep(0.25)
        GPIO.output(led, GPIO.LOW)
        time.sleep(0.25)
    
except KeyboardInterrupt:
    GPIO.cleanup()
