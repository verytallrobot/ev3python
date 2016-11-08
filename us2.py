#!/usr/bin/env python
# us2.py
# senses distance and approaches at full power until nearby then slowly approaches and announces distance to object
# for python2 and ev3dev pre 10


from ev3dev.auto import *
import time


mL = LargeMotor(OUTPUT_B)
mR = LargeMotor(OUTPUT_C)


us = UltrasonicSensor()
assert us.connected, "Connect a US sensor to a numbered port"
us.mode='US-DIST-CM'
distance = us.value()


space = input("What's a safe distance? (Type an integer number of millimetres.)")
space = int(space)


#space = 200
margin = 100
tolerance = 0


space = space + tolerance


while distance > space:
    mL.run_forever(duty_cycle_sp=50)
    mR.run_forever(duty_cycle_sp=50)
    distance = us.value()
    if ((distance < (space + margin)) and (distance > space)):
       # mL.stop()
       # mR.stop()
        mL.run_timed(time_sp=500, duty_cycle_sp=10)
        mR.run_timed(time_sp=500, duty_cycle_sp=10)
        distance = us.value()
        print(str(distance))
#        Sound.speak(str(distance))


mL.stop(stop_action="coast")
mR.stop(stop_action="coast")


Sound.speak("Distance to obstacle" + str(distance) + "milliimeters")
time.sleep(4)


# precision adjustment


distance = us.value()
while distance > space:
        mL.duty_cycle_sp = 5
        mL.run_timed(time_sp = 200)
        distance = us.value()


if distance < space:
    diff = space - distance
    while diff > 10:
        mL.run_timed(time_sp = 100,duty_cycle_sp = -10)
        mR.run_timed(time_sp = 100, duty_cycle_sp = -10)
        distance = us.value()
        diff = space - distance


    while 0 < diff <= 10:
        mL.run_timed(time_sp = 50, duty_cycle_sp = -10)
        mR.run_timed(time_sp = 50, duty_cycle_sp = -10)
        distance = us.value()
        diff = space - distance


distance = us.value()
Sound.speak(str(distance))
