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

    # TODO: this should probably be in an external .py file.
    GPIO.setup(32, GPIO.IN, GPIO.PUD_DOWN)  # flow sensor
    GPIO.setup(33, GPIO.IN, GPIO.PUD_DOWN)  # temperature sensors
    GPIO.setup(35, GPIO.IN, GPIO.PUD_DOWN)  # circulation_punp_button
    GPIO.setup(36, GPIO.IN, GPIO.PUD_DOWN)  # jet_pump_one_button
    GPIO.setup(37, GPIO.IN, GPIO.PUD_DOWN)  # jet_pump_two_button
    GPIO.setup(38, GPIO.IN, GPIO.PUD_DOWN)  # blower_button
    GPIO.setup(40, GPIO.IN, GPIO.PUD_DOWN)  # heater_button


class PhysicalControl:
    def __init__(self):
        self.temp = Temperature()
        self.elements = {
            "circulation_pump": 5,
            "jet_pump_one": 7,
            "jet_pump_two": 8,
            "blower": 10,
            "heater": 11,
            "flow_sensor": 32
        }
        setupGPIO()

    def on(self, key):
        status = GPIO.input(self.elements[key]) == GPIO.HIGH
        print("{} was {}".format(key, status))
        return status

    def turn_on(self, key):
        print("turning on {}".format(key))
        GPIO.input(self.elements[key], 1)

    def turn_off(self, key):
        print("turning off {}".format(key))
        GPIO.output(self.elements[key], 0)

    def air_temp(self):
        self.temperature(self.air_temp_id)

    def water_temp(self):
        self.temperature(self.water_temp_id)

    def flowing(self):
        self.on("flow_sensor")

    @staticmethod
    def max_temp():
        return 106

    def can_turn_on_heat(self):
        return self.flowing() and self.water_temp() <= self.max_temp()

    def turn_on_circulation_pump(self):
        if not self.on('circulation_pump'):
            self.turn_on('circulation_pump')

    def turn_off_circulation_pump(self):
        if self.on("circulation_pump"):
            self.turn_off('circulation_pump')

    def turn_on_jet_pump_one(self):
        if not self.on('jet_pump_one'):
            self.turn_on('jet_pump_one')

    def turn_off_jet_pump_one(self):
        if self.on("jet_pump_one"):
            self.turn_off('jet_pump_one')

    def turn_on_jet_pump_two(self):
        if not self.on('jet_pump_two'):
            self.turn_on('jet_pump_two')

    def turn_off_jet_pump_two(self):
        if self.on("jet_pump_two"):
            self.turn_off('jet_pump_two')

    def turn_on_blower(self):
        if not self.on('blower'):
            self.turn_on('blower')

    def turn_off_blower(self):
        if self.on("blower"):
            self.turn_off('blower')

    def turn_on_heater(self):
        if not self.on('heater'):
            if self.can_turn_on_heat():
                self.turn_on('heater')
            else:
                print("Error: cannot turn on heater!")

    def turn_off_heater(self):
        if self.on("heater"):
            self.turn_off('heater')
