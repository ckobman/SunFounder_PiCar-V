#!/usr/bin/env python

from picar import back_wheels, front_wheels
from remote_control.remote_control.driver import camera, stream
import safe_servo
import picar
import time

picar.setup()
db_file = "/home/pi/SunFounder_PiCar-V/remote_control/remote_control/driver/config"
fw = front_wheels.Front_Wheels(debug=False, db=db_file)
bw = back_wheels.Back_Wheels(debug=False, db=db_file)
#cam = camera.Camera(debug=False, db=db_file)
cam = camera.Camera(debug=False, db=db_file)
cam.ready()

pan  = safe_servo.SafeServo(channel=1, min_angle=0, max_angle=180)

SPEED = 60


bw.ready()
bw.speed = SPEED
fw.ready()

#bw.forward()
#time.sleep(1)
#fw.turn_left()
#time.sleep(1)
#fw.turn_straight()
#time.sleep(1)
#fw.turn_right()
#time.sleep(1)
#fw.turn_straight()
#time.sleep(1)
bw.stop()
#time.sleep(1)


time.sleep(1)
pan.set_angle(0)
time.sleep(1)
for _ in xrange(18):
  pan.adjust_angle(10)
  time.sleep(1)



#bw.speed = SPEED
#bw.backward()
#time.sleep(1)
#fw.turn_left()
#time.sleep(1)
#fw.turn_straight()
#time.sleep(1)
#fw.turn_right()
#time.sleep(1)
#fw.turn_straight()
#time.sleep(1)
#bw.stop()


