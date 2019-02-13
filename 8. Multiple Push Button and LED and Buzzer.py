import RPi.GPIO as GPIO
import time

button1 = 3
button2 = 5
led = 11
buzzer = 13

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(buzzer, GPIO.OUT)

print("Key Pad is ready")

while True:
    input_state_button1 = GPIO.input(button1)
    input_state_button2 = GPIO.input(button2)
    if input_state_button1 == False:
        GPIO.output(led, 1)
        print('Button 1 is Pressed')
        time.sleep(0.2)
        
    elif input_state_button2 == False:
        GPIO.output(buzzer, 1)
        print('Button 2 is Pressed')
        time.sleep(0.2)
        
        
    else:
        GPIO.output(buzzer, 0)
        GPIO.output(led, 0)
   
