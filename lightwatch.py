import RPi.GPIO as GPIO
import time

def start_measure(): 
	return time.time()

def end_measure(starttime):
	endtime = time.time()
	duration = endtime - starttime
	return duration

def isSunBurning():
	if GPIO.input(9) == 0:
		return bool(1)
	else:
		return bool(0)

def isLightOn():
	if GPIO.input(4) == 0:
		much_light = bool(1)
	else:
		much_light = bool(0)
	return much_light

#Set up GPIO mode and define the pins
GPIO.setmode(GPIO.BCM)
# Set up the pin
GPIO.setup(9,GPIO.IN)
help_bool = False
while True:
	if help_bool == False:
		start = time.time()
		help_bool = True
	if not isSunBurning():
		help_bool = False
		break
time.sleep(1)
duration = time.time() - start
print(duration, " secconds")



#Set up GPIO mode and define the pins
GPIO.setmode(GPIO.BCM)
# Set up the pin
GPIO.setup(4,GPIO.IN)
help_bool = False
while True:
	if help_bool == False:
		start = time.time()
		help_bool = True
	if not isLightOn():
		help_bool = False
		break
time.sleep(1)
#print(time.strftime("%H:%M:%S", time.gmtime(start)))
#print(time.strftime("%H:%M:%S", time.gmtime(time.time())))
duration = time.time() - start
print(duration, " secconds")

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
