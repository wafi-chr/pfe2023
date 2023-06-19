from time import sleep
# from degres import *
import RPi.GPIO as GPIO
#from belectro import *
def  retour_fonction(degress):
    DIR = 21   # Direction GPIO Pin
    STEP = 20  # Step GPIO Pin
    CW = 0 # Clockwise Rotation
    CCW = 1   # Counterclockwise Rotation
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(DIR, GPIO.OUT)
    GPIO.setup(STEP, GPIO.OUT)
#     deg_step=input('donnez le degres')
    SPR=degress
    delay = .0100   
    step_count = int(SPR)
    GPIO.output(DIR, CCW)
    for x in range(step_count):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay) 
        print('fin du programme deg')
      
      
    