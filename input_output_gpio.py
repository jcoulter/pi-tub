#!/usr/bin/env python3
# import RPi.GPIO as GPIO


def setupGPIO():


    # GPIO.setmode(GPIO.BCM)
    # GPIO.setwarnings(False)
    #
    # GPIO.setup(18, GPIO.OUT)

class InOut:
    def __init__(self):
        self.water_temp_id = '28-012063bee088'
        self.air_temp_id = '28-012063c43c9d'
        setupGPIO()

    @staticmethod
    def temperature(sensor_id):
        temp_store = open("/sys/bus/w1/devices/{}/w1_slave").format(sensor_id)
        raw_temp = temp_store.read()
        temp_store.close()
        temp = float(raw_temp.split("\n")[1].split(" ")[9][2:])
        c_temp = temp / 1000
        (c_temp * 9 / 5) + 32

    def air_temp(self):
        self.temperature(self.air_temp_id)

    def water_temp(self):
        self.temperature(self.water_temp_id)

    @staticmethod
    def flowing():
        return True

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
