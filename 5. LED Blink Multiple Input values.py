import RPi.GPIO as GPIO
import time

led = 3

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT)
GPIO.output(led, 0)

BlinkTimes = input("How many times LED shoud Blink ? \n")
OnTime = input("Enter LED on duration \n")
OffTime = input("Enter LED off duration \n")

print("LED will blink for ", BlinkTimes)

for i in range(int(BlinkTimes)):
    GPIO.OUT(led, 1)
    time.sleep(int(OnTime))
    GPIO.OUT(led, 0)
    time.sleep(int(OffTime))
    print(str(i+1) + " times blinked")