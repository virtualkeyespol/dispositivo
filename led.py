import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

## ACTUALIZADO - NARANJA
GPIO.setup(4, GPIO.OUT)

## ABIERTO - VERDE
GPIO.setup(17, GPIO.OUT)

## STATUS - AZUL
GPIO.setup(27, GPIO.OUT)

def actualizado():
	for i in range(0,3):	
		GPIO.output(4, True)
		time.sleep(0.3)
		GPIO.output(4, False)
		time.sleep(0.3)

def abierto():
	GPIO.output(17, True)
	time.sleep(1)
	GPIO.output(17, False)


def status():
	GPIO.output(27, True)
	time.sleep(1)
	GPIO.output(27, False)
