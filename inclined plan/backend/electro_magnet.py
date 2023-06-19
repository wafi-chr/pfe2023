
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
def magnet(a):
    ELCTR =3  #Définit le numéro du port GPIO qui alimente la led
    GPIO.setup(ELCTR, GPIO.OUT) #Active le contrôle du GPI
    #print('elctro')
    if a==1:
        GPIO.output(ELCTR, GPIO.HIGH)
        print('elctro is on')
    else:
        GPIO.output(ELCTR, GPIO.LOW)
        print('elctro is off')
    

#magnet(1)


  