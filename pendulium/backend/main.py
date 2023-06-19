from ahome import *
from dfin import*
from belectro import *
from cdeg import *
from start import*
from time import sleep
import RPi.GPIO as GPIO
while True:
      GPIO.cleanup()
      home_fonction()
      time.sleep(1)
      degres_fonction(50)
      time.sleep(5)
      start_fonction()
      #
      #fin_fonction() 
    