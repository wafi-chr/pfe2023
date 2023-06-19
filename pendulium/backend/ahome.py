from time import sleep
import time
from cdeg import *
from belectro import *
import RPi.GPIO as GPIO #Importe la bibliothèque pour contrôler les GPIOs
def home_fonction():
    GPIO.setmode(GPIO.BCM)
    LimitSwitch = 4
    GPIO.setup(LimitSwitch, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    SPR=72
    RSPR=22
    DIR = 21   # Direction GPIO Pin
    STEP = 20  # Step GPIO Pin
    CW = 0 # Clockwise Rotation
    CCW = 1    # Counterclockwise Rotation
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(DIR, GPIO.OUT)
    GPIO.setup(STEP, GPIO.OUT)
    delay = .0100
    step_count = int(SPR)
    for x in range(step_count):                    
                    if     GPIO.input(LimitSwitch) == 0:   
                           print("pressed")#### si le fin de course est presse le moteur s'arrete
                           break                           
                    else:                           
                           print("not pressed") #### si le fin de course est presse le moteur tourne
                           GPIO.output(DIR, CW)
                           GPIO.output(STEP, GPIO.HIGH)
                           sleep(delay)
                           GPIO.output(STEP, GPIO.LOW)
                           sleep(delay) 
    
    elctro_fonction(1)
    time.sleep(0.5)
    
    for x in range(RSPR):                                                               
        print("reverse") #### si le fin de course est presse le moteur tourne
        GPIO.output(DIR, CCW)
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay) 
    
    print('fin du programme home')               
               
                
  
    
    