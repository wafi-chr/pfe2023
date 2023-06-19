from electro_magnet import *
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False) #On désactive les messages d'alerte
s1 = 14  #Définit le numéro du port GPIO qui alimente la led 
s2 = 15
s3 = 7
s4 = 24
GPIO.setup(s1, GPIO.IN) #Active le contrôle du GPI
GPIO.setup(s2, GPIO.IN) #Active le contrôle du GPI
GPIO.setup(s3, GPIO.IN) #Active le contrôle du GPI 
GPIO.setup(s4, GPIO.IN)

def start_timers():
    print("---------Start Timers-------------------")
    t0=0
    t1=0
    t2=0
    t3=0
    t4=0
    magnet(0)
    t0=time.time()
    t0=round(t0, 2)
    
    while True:
        if GPIO.input(s4)==0:
            print('object detected s4')
            t4=time.time()
            t4=round(t4-t0, 2)
            print("temps 4 :",t4)
            sleep(.05)
            break
        if GPIO.input(s1)==0:
            print('object detected s1')
            t1=time.time()
            t1=round(t1-t0, 2)
            print("temps 1 :",t1)
            sleep(1)
        if GPIO.input(s2)==0:
            print('object detected s2')
            t2=time.time()
            t2=round(t2-t0, 2)
            print("temps 2 :",t2)
            sleep(1)
        if GPIO.input(s3)==0:
            print('object detected s3')
            t3=time.time()
            t3=round(t3-t0, 2)
            print("temps 3 :",t3)
            sleep(1)    
            
    # print("temps 0 :",t0)
    print("temps 1 :",t1)
    print("temps 2 :",t2)
    print("temps 3 :",t3)
    print("temps 4 :",t4)
    
    return t1,t2,t3,t4  
#start_timers()    
    