import FaBo9Axis_MPU9250
import time
import sys
import json
def gyro_fonction():
    compteur = 0
    start = 0
    mpu9250 = FaBo9Axis_MPU9250.MPU9250()
    ax0=-0.019
    dataObj =[] 
    try:
      while compteur <= 125:
          accel = mpu9250.readAccel()
          print ( " ay = ", ( accel['y']))
          gyro = mpu9250.readGyro()
          print ( " gy = " ,( gyro['y']  ))
          compteur = compteur + 1
          time.sleep(0.2)
          start = start + 0.2
          dataObj.append({"x":start, "Ay": accel['y'], "Vy": gyro['y']})
        
         # print("stop")
            #break  
     # time.sleep(0.2)
      print (compteur)
      return dataObj
    except KeyboardInterrupt:
     sys.exit()
