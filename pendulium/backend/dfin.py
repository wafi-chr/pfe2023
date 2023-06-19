from time import sleep
import time
import RPi.GPIO as GPIO #Importe la bibliothèque pour contrôler les GPIOs
def fin_fonction():
    GPIO.setmode(GPIO.BCM)
    Switch = 17
    GPIO.setup(Switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    while True:
                       if     GPIO.input(Switch) == 0:   
                              print("presse de fin")#### si le fin de course est presse le moteur s'arrete
                              break                           
                       else:                           
                           print("not pressed de fin") #### si le fin de course est presse le moteur tourne                                                      
    
