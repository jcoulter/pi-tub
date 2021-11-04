#!/usr/bin/env python3
import RPi.GPIO as GPIO
from physical_control as PhysicalControl

try:
    while 1 >= 0:


except KeyboardInterrupt:  # Stops program when "Control + C" is entered
    GPIO.cleanup()  # Turns OFF all relay switches

