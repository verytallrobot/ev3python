#!/usr/bin/env python
from ev3dev.auto import *
from time import sleep


mR = Motor('outB')
mL = Motor('outD')


us = UltrasonicSensor()
assert us.connected, "Connect a single infrared sensor to any sensor port"


target = 350
tolerance = 5
target = target + tolerance
margin = 100
distance = us.value()
while distance >= target+margin:
       mR.run_forever(duty_cycle_sp = 100)
                   #mL.run_to_rel_pos(position_sp=360, speed_sp=900)
       mL.run_forever(duty_cycle_sp=100)
                   #time.sleep(5)   # Give the motor time to move
                   #mL.stop()
       distance = us.value()
       while ((distance < target+margin) and (distance > target)):
          mR.run_forever(duty_cycle_sp = 30)
                   #mL.run_to_rel_pos(position_sp=360, speed_sp=900)
          mL.run_forever(duty_cycle_sp=30)
                   #time.sleep(5)   # Give the motor time to move
                   #mL.stop()
          distance = us.value()


mL.stop(stop_action='hold')
mR.stop(stop_action='hold')
Sound.speak("Distance to obstacle is" + str(distance) +" M m")
sleep(5)
distance = us.value()
Sound.speak("Distance to obstacle is" + str(distance) +" M m")
