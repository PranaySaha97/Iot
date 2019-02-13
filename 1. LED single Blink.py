import RPi.GPIO as GPIO
import time

led = 3

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT)
GPIO.output(led, GPIO.LOW)


print"LED Blink"

GPIO.output(led, GPIO.HIGH)
time.sleep(1)
GPIO.output(led, GPIO.LOW)
time.sleep(1)








