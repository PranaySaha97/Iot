import RPi.GPIO as GPIO
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11           
pin = 3
GPIO.setwarnings(False)

try:
    print("Temperature Sensor is getting ready")
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        if humidity is not None and temperature is not None:
            print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
        else:
            print('Failed to get reading. Try again!')

except KeyboardInterrupt:                                                              # Reset by pressing CTRL + C
    print("Measurement stopped by User")
    GPIO.cleanup()
