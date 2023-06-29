import RPi.GPIO as GPIO
import time

def rotation():
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
    duration = 0.05
    for i in range(20):
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
    # Clean up GPIO
    GPIO.cleanup()

print("vor rotation")
rotation()
print("nach rotation")
