#!/usr/bin/env python3
# m3.py
# check that the kernel and version of python are right for running this new class of motor methods. Connect a large motor to output B.


from ev3dev.ev3 import *
from time import sleep


m = LargeMotor('outB')
m.stop_action="hold"

m.run_to_rel_pos(position_sp=360, speed_sp=900)


sleep(5)   # Give the motor time to move
