import RPi.GPIO as GPIO
import time

button = 5
led = 3

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led, GPIO.OUT)

print("Key Pad is ready")

while True:
    input_state = GPIO.input(push button)
    if input_state == False:
        GPIO.output(led, 1)
        print('Button Pressed')
        time.sleep(0.2)
    else:
        GPIO.output(led, 0)



    