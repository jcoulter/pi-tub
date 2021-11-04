#!/usr/bin/env python3


class InOut:
    def __init__(self):
        self.water_temp_id = '28-012063bee088'
        self.air_temp_id = '28-012063c43c9d'
        self.circulation_pump = False
        self.jet_pump_one = False
        self.jet_pump_two = False
        self.blower = False
        self.heater = False

    @staticmethod
    def temperature(sensor_id):
        temp_store = open("/sys/bus/w1/devices/{}/w1_slave").format(sensor_id)
        raw_temp = temp_store.read()
        temp_store.close()
        temp = float(raw_temp.split("\n")[1].split(" ")[9][2:])
        c_temp = temp / 1000
        f_temp = (c_temp * 9 / 5) + 32

    @staticmethod
    def air_temp():
        return 76

    @staticmethod
    def water_temp():
        return 106

    @staticmethod
    def flowing():
        return False

    @staticmethod
    def max_temp():
        return 106

    def can_turn_on_heat(self):
        return self.flowing() and self.water_temp() <= self.max_temp()

    def turn_on_circulation_pump(self):
        if self.circulation_pump:
            print("circulation_pump was already on")
        else:
            print("self.circulation_pump = {}".format(self.circulation_pump))
            print("turning on circulation_pump")
            self.circulation_pump = True

    def turn_off_circulation_pump(self):
        if not self.circulation_pump:
            print("circulation_pump was already off")
        else:
            print("self.circulation_pump = {}".format(self.circulation_pump))
            print("turning off circulation_pump")
            self.circulation_pump = False

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

    def turn_on_heater(self):
        if self.can_turn_on_heat():
            print("turning on heater")
        else:
            print("error, cannot turn on heat!")

    @staticmethod
    def turn_off_heater():
        print("turning off heater")
