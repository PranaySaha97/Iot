import RPi.GPIO as GP
import time

led = 3

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT)
GPIO.output(led, 0)

print("LED Blinking....")

while True:
    GPIO.output(led, 1)
    time.sleep(1)
    GPIO.output(led, 0)
    time.sleep(1)
	
