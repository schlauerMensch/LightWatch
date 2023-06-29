import RPi.GPIO as GPIO
import time

# Pin-Nummern anpassen, je nachdem welche GPIO-Pins Sie verwenden
PIN_RED = 16
PIN_GREEN = 20
PIN_BLUE = 21

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)

# Set up the pins
GPIO.setup(PIN_RED, GPIO.OUT)
GPIO.setup(PIN_GREEN, GPIO.OUT)
GPIO.setup(PIN_BLUE, GPIO.OUT)

# Function to turn on the LED with specified color
def turn_on(color):
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

# Example usage
d = 0.05
for i in range(10):
	turn_on('red')
	time.sleep(d)  # Wait for 1 second
	turn_on('green')
	time.sleep(d)
	turn_on('blue')
	time.sleep(d)
	turn_on('yellow')
	time.sleep(d)
	turn_on('purple')
	time.sleep(d)
	turn_on('cyan')
	time.sleep(d)
	turn_on('white')
	time.sleep(d)
	turn_on('off')  # Turn off all LEDs

# Clean up GPIO
GPIO.cleanup()
