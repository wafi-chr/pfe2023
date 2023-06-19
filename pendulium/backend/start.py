from belectro import *
from dfin import *
import time
def start_fonction():
    elctro_fonction(0)
    t1=time.time()
    print("temps 1 :",t1)
    fin_fonction()
    ###arreter le timer
    t2=time.time()
    t3=t2-t1
    print("temps golabal",t3)
    return t3