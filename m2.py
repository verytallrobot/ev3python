# Test program for older version of ev3dev running python2
from ev3dev.auto import OUTPUT_B, Motor
import time


m = Motor(OUTPUT_B)
m.run_forever(duty_cycle_sp = 100)
time.sleep(1)
m.stop()
