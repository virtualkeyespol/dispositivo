import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

## ACTUALIZADO
GPIO.setup(4, GPIO.OUT)

def actualizado():
	for i in range(0,3):	
		GPIO.output(4, True)
		time.sleep(0.3)
		GPIO.output(4, False)
		time.sleep(0.3)