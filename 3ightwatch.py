import RPi.GPIO as GPIO
import time
import requests

def setup():
    # Pin-Nummern anpassen, je nachdem welche GPIO-Pins Sie verwenden
    PIN_RED = 16
    PIN_GREEN = 20
    PIN_BLUE = 21
    PIN_SUN = 9
    PIN_LIGHT = 4
    # Set up GPIO mode
    GPIO.setmode(GPIO.BCM)
    # Set up the pins
    GPIO.setup(PIN_RED, GPIO.OUT)
    GPIO.setup(PIN_GREEN, GPIO.OUT)
    GPIO.setup(PIN_BLUE, GPIO.OUT)
    GPIO.setup(PIN_SUN, GPIO.IN)
    GPIO.setup(PIN_LIGHT, GPIO.IN)
def turn_on(color):
    PIN_RED = 16
    PIN_GREEN = 20
    PIN_BLUE = 21
    if color == 'red':
        GPIO.output(PIN_RED, GPIO.HIGH)
        GPIO.output(PIN_GREEN, GPIO.LOW)
        GPIO.output(PIN_BLUE, GPIO.LOW)
    elif color == 'green':
        GPIO.output(PIN_RED, GPIO.LOW)
        GPIO.output(PIN_GREEN, GPIO.HIGH)
        GPIO.output(PIN_BLUE, GPIO.LOW)
    elif color == 'blue':
        GPIO.output(PIN_RED, GPIO.LOW)
        GPIO.output(PIN_GREEN, GPIO.LOW)
        GPIO.output(PIN_BLUE, GPIO.HIGH)
    elif color == 'yellow':
        GPIO.output(PIN_RED, GPIO.HIGH)
        GPIO.output(PIN_GREEN, GPIO.HIGH)
        GPIO.output(PIN_BLUE, GPIO.LOW)
    elif color == 'purple':
        GPIO.output(PIN_RED, GPIO.HIGH)
        GPIO.output(PIN_GREEN, GPIO.LOW)
        GPIO.output(PIN_BLUE, GPIO.HIGH)
    elif color == 'cyan':
        GPIO.output(PIN_RED, GPIO.LOW)
        GPIO.output(PIN_GREEN, GPIO.HIGH)
        GPIO.output(PIN_BLUE, GPIO.HIGH)
    elif color == 'white':
        GPIO.output(PIN_RED, GPIO.HIGH)
        GPIO.output(PIN_GREEN, GPIO.HIGH)
        GPIO.output(PIN_BLUE, GPIO.HIGH)
    else:
        # Invalid color, turn off all LEDs
        GPIO.output(PIN_RED, GPIO.LOW)
        GPIO.output(PIN_GREEN, GPIO.LOW)
        GPIO.output(PIN_BLUE, GPIO.LOW)
def rotation():
    duration = 0.02
    for i in range(5):
        turn_on('red')
        time.sleep(duration)
        turn_on('green')
        time.sleep(duration)
        turn_on('blue')
        time.sleep(duration)
        turn_on('yellow')
        time.sleep(duration)
        turn_on('purple')
        time.sleep(duration)
        turn_on('cyan')
        time.sleep(duration)
        turn_on('white')
        time.sleep(duration)
        turn_on('off')  # Turn off all LEDs
def sunIsBurning():
    PIN_SUN = 9
    if GPIO.input(PIN_SUN) == 0:
        return True
    else:
        return False
def lightIsOn():
    PIN_LIGHT = 4
    if GPIO.input(PIN_LIGHT) == 0:
        return True
    else:
        return False
def rek1():
    while True:
        if sunIsBurning() and lightIsOn():
            start = time.time()
            rotation()
            end = rek2()
            duration = end - start
            print("Duration: ", duration)
            data = {'sekunden': duration, 'klasse': 'Klasse A'}
            response = requests.post("http://mdserver/Lightwatch/index.php", data=data)
            break
def rek2():
    while True:
        if sunIsBurning() and not lightIsOn():
            return time.time()
# Set up GPIO
setup()
while True:
	rek1()
