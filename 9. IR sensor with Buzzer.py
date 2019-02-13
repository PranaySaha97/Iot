import RPi.GPIO as GPIO
import time

IRsensor = 5
buzzer = 3

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(IRsensor,GPIO.IN)
GPIO.setup(buzzer, GPIO.OUT)


while True:
    input_state = GPIO.input(IRsensor)
    if input_state == 1:
        GPIO.output(buzzer, 1)
        print("Obstacle Detected")
        time.sleep(0.5)
    else:
        print("No Obstacle Detected")
        GPIO.output(buzzer, 0)





