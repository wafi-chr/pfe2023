from time import sleep
import time
from stepper import *
from electro_magnet import *
import RPi.GPIO as GPIO #Importe la bibliothèque pour contrôler les GPIOs

def home():
    GPIO.setmode(GPIO.BCM)
    LimitSwitch = 16
    GPIO.setup(LimitSwitch, GPIO.IN)
    SPR=72
    RSPR=22
    delay = .0100
    step_count = int(SPR)
    for x in range(step_count):                    
        if GPIO.input(LimitSwitch) == 0:   
            #print("last switch pressed")#### si le fin de course est presse le moteur s'arrete
            break                           
        else:                           
            #print("last sensor not pressed") #### si le fin de course est presse le moteur tourne
            turn(2,0)               
    print("-----------------------------------")            
    magnet(1)
    sleep(1)
    for x in range(RSPR):                                                               
        #print("reverse") #### si le fin de course est presse le moteur tourne
        turn(2,1)

                  
#home_fonction()
    