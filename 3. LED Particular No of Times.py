import RPi.GPIO as GPIO
import time

led = 3
BlinkTimes = 5

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT)
GPIO.output(led, 0)

print("LED will blink for ", BlinkTimes)

for i in range(BlinkTimes):
	GPIO.output(led, 1)
	sleep(1)
	GPIO.output(led, 0)
	sleep(1)
	