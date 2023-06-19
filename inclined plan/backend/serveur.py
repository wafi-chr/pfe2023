from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import json
import sys
import RPi.GPIO as GPIO

from home import *
from timers import *
from stepper import *

from time import sleep
port = 8081
class SimpleEcho(WebSocket):
    
    def handleMessage(self):
        Data = json.loads(self.data)
        print(self.data)

        if Data["message"] in ["start"]:
            print('start pressed')
            t1,t2,t3,t4 = start_timers()
            res = str(t1) + "s" + " " + str(t2) + "s" + " " + str(t3) + "s"+ " " + str(t4) + "s"
            print(res)
            #strtime = str(resultat)
            self.sendMessage(res)
            #home()

        if Data["message"] in ["reset"]:
            print('reset')
            home()
               
        if Data["message"] in ["degres"]:
            print('degres presse')
            degress=float(Data["degres"])
            print(degress)
            home()
            sleep(1)
            turn(degress,1)
        #homed = False
               
               
    def handleConnected(self):
        print(self.address,'connected')

    def handleClose(self):
        print(self.address,'closed')
                 
#def programme_golbal():
   # main()

server = SimpleWebSocketServer('', port, SimpleEcho)
server.serveforever()

