from time import sleep
import RPi.GPIO as GPIO #Importe la bibliothèque pour contrôler les GPIOs
from ahome import *
def fin_fonction():
	GPIO.setmode(GPIO.BCM)
	Switch = 16
	GPIO.setup(Switch, GPIO.IN)
	while True:
		sleep(.5)
		if GPIO.input(Switch) == 0 :
			print("presse de fin")#### si le fin de course est presse le moteur s'arrete
			break                           
		else:                           
			print("not pressed de fin") #### si le fin de course est presse le moteur tourne                                                      

#fin_fonction()
