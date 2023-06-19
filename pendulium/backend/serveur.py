from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import json
import sys
import RPi.GPIO as GPIO
# from ahome import *
from belectro import *
from cdeg import *
from retour import *
# from start import *
from time import sleep
GPIO.setwarnings(False) #On désactive les messages d'alerte
ELCTR =12 #Définit le numéro du port GPIO qui alimente la led
GPIO.setmode(GPIO.BCM)
GPIO.setup(ELCTR, GPIO.OUT) #Active le contrôle du GPI
port = 8081
class SimpleEcho(WebSocket):
    def handleMessage(self):
        Data = json.loads(self.data)
        print(self.data)
        if Data["message"] in ["start"]:
           print('START')
           result = elctro_fonction(0)
           self.sendMessage(json.dumps(result))
           print(result)
                       
        if Data["message"] in ["reset"]:
           print('RESETT')
           GPIO.output(ELCTR, GPIO.HIGH)
           degress=float(Data["degres"])
           retour_fonction(degress)
           
        if Data["message"] in ["degres"]:
           degress=float(Data["degres"])
           print(degress)
           elctro_fonction(1)
           degres_fonction(degress)
           print('degres presse')
           
           
    def handleConnected(self):
        print(self.address,'connected')

    def handleClose(self):
        print(self.address,'closed')
                 
#def programme_golbal():
   # main()
server = SimpleWebSocketServer('', port, SimpleEcho)
server.serveforever()

