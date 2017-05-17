#!/usr/bin/env python

from picar.SunFounder_PCA9685 import Servo
import time

class SafeServo(object):
  
  def __init__(self, channel, initial_angle=90, min_angle=0, max_angle=180):
    self.servo = Servo.Servo(channel) 
    self.channel = channel
    self.min_angle = min_angle
    self.max_angle = max_angle
    self.current_angle = initial_angle
    self.move()

  def set_angle(self, angle):
    self.current_angle = angle
    self.move()

  def adjust_angle(self, adjustment):
    self.current_angle = self.current_angle + adjustment
    self.move()

  def move(self):
    if self.current_angle > self.max_angle:
      print 'Channel', self.channel, 'attempted to set', self.current_angle, 'max allowed angle is', self.max_angle
      self.servo.write(self.max_angle)
    elif self.current_angle < self.min_angle:
      print 'Channel', self.channel, 'attempted to set', self.current_angle, 'min allowed angle is', self.min_angle
      self.servo.write(self.min_angle)
    else:
      self.servo.write(self.current_angle)
