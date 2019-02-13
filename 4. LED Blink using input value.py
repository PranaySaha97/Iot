import RPi.GPIO as GPIO
import time

led = 3


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT)
GPIO.output(led, 0)

BlinkTimes = input("How many times LED shoud Blink ? \n")

print("LED will blink for ", BlinkTimes)

for i in range(int(BlinkTimes)):
    GPIO.output(led, 1)
    time.sleep(1)
    GPIO.output(led, 0)
    time.sleep(1)
    print( (i+1) + " times blinked")














