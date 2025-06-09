#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


mB = Motor(Port.B)
mC = Motor(Port.C)

mB.run(250)

wait(8000)
mB.brake()



mB.run(300)
mC.run(100)


wait(7000)
mB.brake()
mC.brake()




mB.run(300)
mC.run(-300)


wait(7000)
mB.brake()
mC.brake()





# Write your program here.
ev3.speaker.beep()
