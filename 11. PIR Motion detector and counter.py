import RPi.GPIO as GPIO
import time

PIRsensor = 5
buzzer = 3
count = 0

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIRsensor, GPIO.IN)
GPIO.setup(buzzer, GPIO.OUT)

print("Motion Detector is getting ready")
time.sleep(2) 
print("Motion Detector is ready")

while True:
    input_state = GPIO.input(PIRsensor)
    if input_state == 1:
        GPIO.output(buzzer, 1)
        time.sleep(0.5)
        GPIO.output(buzzer, 0)
        time.sleep(3)
        count = count+1
        print("Motion Detected " + str(count) + " times")

    else:
        GPIO.output(buzzer, 0)






