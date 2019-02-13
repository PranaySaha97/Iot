import RPi.GPIO as GPIO
import time

button = 5

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print("Key Pad is ready")

while True:
    input_state = GPIO.input(button)
    if input_state = False:
        print('Button Pressed')
        time.sleep(0.2)



    