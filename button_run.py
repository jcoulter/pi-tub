#!/usr/bin/env python3
import RPi.GPIO as GPIO
from physical_control import PhysicalControl
import time

try:
    phys = PhysicalControl()
    while 1 >= 0:
        print("waiting")
        time.sleep(0.5)

except KeyboardInterrupt:  # Stops program when "Control + C" is entered
    GPIO.cleanup()  # Turns OFF all relay switches

