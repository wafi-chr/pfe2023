import time
#from ahome import *
from time import sleep
from gyro import *
import RPi.GPIO as GPIO
a=1
def elctro_fonction(a):
    GPIO.setwarnings(False) #On désactive les messages d'alerte
    ELCTR =12 #Définit le numéro du port GPIO qui alimente la led
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ELCTR, GPIO.OUT) #Active le contrôle du GPI
    print('elctro')
    if a==1:
      GPIO.output(ELCTR, GPIO.HIGH)
      print('elctro is on')
      
    else:
      GPIO.output(ELCTR, GPIO.LOW)
      print('elctro is off')
      data = gyro_fonction()
      return data
    



  