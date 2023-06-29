import RPi.GPIO as GPIO
import time
import requests

#Set up GPIO mode and define the pins
GPIO.setmode(GPIO.BCM)
# Set up the pin
GPIO.setup(9,GPIO.IN)
#Set up GPIO mode and define the pins
GPIO.setmode(GPIO.BCM)
# Set up the pin
GPIO.setup(4,GPIO.IN)

def start_measure():
	return time.time()

def end_measure(starttime):
	endtime = time.time()
	duration = endtime - starttime
	return duration

def sunIsBurning():
#	GPIO.setmode(GPIO.BCM)
	if GPIO.input(9) == 0:
		return bool(1)
	else:
		return bool(0)

def lightIsOn():
#	GPIO.setmode(GPIO.BCM)
	if GPIO.input(4) == 0:
		much_light = bool(1)
	else:
		much_light = bool(0)
	return much_light


#help_bool = not sunIsBurning()
def rek1():
	while True:
		if (sunIsBurning() and lightIsOn()):
			start = time.time()
			end = rek2()
			duration = end-start
			print("Duration: ", duration)
			data = {'duration': duration}
			response = requests.post("http://mdserver/Lightwatch/index.php", data=data)
			break
def rek2():
	while True:
		if (sunIsBurning() and (not lightIsOn())):
			return time.time()
while True:
	rek1()
#		break
#print(time.strftime("%H:%M:%S", time.gmtime(start)))
#print(time.strftime("%H:%M:%S", time.gmtime(time.time())))
#duration = time.time() - start
#print(duration, " secconds")

#print("Programm abgeschlossen Die Lampe war " + str("{:.2f}".format(end_measure(start) * 1000)) + " Sekunden an")

#	while !much_light:
#		print("a")

#try:
 #   while True:
  #      light = GPIO.input(light_sensor_pin)
   #     if light == GPIO.HIGH:
    #        GPIO.output(led_pin, GPIO.HIGH)
     #   else:
      #      GPIO.output(led_pin, GPIO.LOW)
#except KeyboardInterrupt:
 #   GPIO.cleanup()
