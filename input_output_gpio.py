#!/usr/bin/env python3
import RPi.GPIO as GPIO
from temperature import Temperature


def setupGPIO():
    GPIO.setmode(GPIO.BOARD)  # the pin numbers refer to the board connector not the chip
    GPIO.setwarnings(False)

    # OUTPUT
    GPIO.setup(3, GPIO.OUT)
    GPIO.setup(5, GPIO.OUT)  # circulation pump
    GPIO.setup(7, GPIO.OUT)  # jet_pump_one
    GPIO.setup(8, GPIO.OUT)  # jet_pump_two
    GPIO.setup(10, GPIO.OUT)  # blower
    GPIO.setup(11, GPIO.OUT)  # heater

    # INPUT - pulled up with resistor

    # GPIO.setup(31, GPIO.IN, GPIO.PUD_UP)
    # GPIO.setup(32, GPIO.IN, GPIO.PUD_UP)

    # GPIO.output(11, GPIO.HIGH)
    # GPIO.setup(13, GPIO.OUT)
    # GPIO.output(13, GPIO.HIGH)
    # GPIO.setup(15, GPIO.OUT)
    # GPIO.output(15, GPIO.HIGH)

    # GPIO.setmode(GPIO.BCM)
    # GPIO.setwarnings(False)
    #
    # GPIO.setup(18, GPIO.OUT)


class InOut:
    def __init__(self):
        self.temp = Temperature()
        setupGPIO()

    def air_temp(self):
        self.temp.air_temp()

    def water_temp(self):
        self.temp.water_temp()

    @staticmethod
    def flowing():
        return True

    @staticmethod
    def max_temp():
        return 106

    def can_turn_on_heat(self):
        return self.flowing() and self.water_temp <= self.max_temp

    # All of these should check if they are already in the desired state or not.
    # They should also check for any preconditions for firing.

    @staticmethod
    def turn_on_circulation_pump():
        print("turning on circulation_pump")

    @staticmethod
    def turn_off_circulation_pump():
        print("turning off circulation_pump")

    @staticmethod
    def turn_on_jet_pump_one():
        print("turning on jet_pump_one")

    @staticmethod
    def turn_off_jet_pump_one():
        print("turning off jet_pump_one")

    @staticmethod
    def turn_on_jet_pump_two():
        print("turning on jet_pump_two")

    @staticmethod
    def turn_off_jet_pump_two():
        print("turning off jet_pump_two")

    @staticmethod
    def turn_on_blower():
        print("turning on blower")

    @staticmethod
    def turn_off_blower():
        print("turning off blower")

    # Turn on circulation pump, check flow sensor
    @staticmethod
    def turn_on_heater():
        print("turning on heater")

    @staticmethod
    def turn_off_heater():
        print("turning off heater")
