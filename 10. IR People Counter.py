import RPi.GPIO as GPIO
import time

IRsensor = 5
buzzer = 3
count = 0

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(IRsensor, GPIO.IN)
GPIO.setup(buzzer, GPIO.OUT)


while True:
    input_state = GPIO.input(IRsensor)
    time.sleep(0.5)
    if input_state == 1:
        input_state_1 = GPIO.input(IRsensor)
        if input_state_1 == 0:
            count = count+1
            GPIO.output(buzzer, 1)
            time.sleep(0.5)
        print("Obstacle Detected " + str(count) + " times")
        
    else:
        GPIO.output(buzzer, 0)





