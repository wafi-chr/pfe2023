from sys import argv
from time import sleep
#from degres import *
import RPi.GPIO as GPIO
def turn(deg_step,dir):
        DIR = 21   # Direction GPIO Pin
        STEP = 20  # Step GPIO Pin
        CW = 0 # Clockwise Rotation
        CCW = 1    # Counterclockwise Rotation
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(DIR, GPIO.OUT)
        GPIO.setup(STEP, GPIO.OUT)
    #DEG=input('donnez le degres')
        SPR=deg_step/1.8
        delay = .0070
        if dir:
            GPIO.output(DIR, CCW)
        else:
            GPIO.output(DIR, CW)
            
        step_count = int(SPR)
        for x in range(step_count):
             GPIO.output(STEP, GPIO.HIGH)
             sleep(delay)
             GPIO.output(STEP, GPIO.LOW)
             sleep(delay) 
        return "fin du programme deg"

#turn(200,1)
# def degres(deg_step,dir):
#         DIR = 21   # Direction GPIO Pin
#         STEP = 20  # Step GPIO Pin
#         CW = 0 # Clockwise Rotation
#         CCW = 1    # Counterclockwise Rotation
#         GPIO.setmode(GPIO.BCM)
#         GPIO.setup(DIR, GPIO.OUT)
#         GPIO.setup(STEP, GPIO.OUT)
#         if dir:
#             GPIO.output(DIR, GPIO.HIGH)
#         else:
#              GPIO.output(DIR, GPIO.LOW)
#     #DEG=input('donnez le degres')
#         SPR=deg_step/1.8
#         #SPR=deg_step
#         delay = .0050
    
#         step_count = int(SPR)
#         for x in range(step_count):
#              GPIO.output(STEP, GPIO.HIGH)
#              sleep(delay)
#              GPIO.output(STEP, GPIO.LOW)
#              sleep(delay) 
#         return "fin du programme deg"


# if __name__=="__main__":    
#     print(argv[2])
#     if len(argv)>1:
#         print(f'Deg= {argv[1]}')
#         degres(float(argv[1]),int(argv[2]))

#     else:
#         degres_fonction(100)

