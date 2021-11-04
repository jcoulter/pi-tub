#!/usr/bin/env python3

#             print("self.heater = {}".format(self.heater))

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
        return True

    @staticmethod
    def max_temp():
        return 106

    def can_turn_on_heat(self):
        return self.flowing() and self.water_temp() <= self.max_temp()

    def turn_on_circulation_pump(self):
        if self.circulation_pump:
            print("circulation_pump was already on")
        else:
            print("turning on circulation_pump")
            self.circulation_pump = True

    def turn_off_circulation_pump(self):
        if not self.circulation_pump:
            print("circulation_pump was already off")
        else:
            print("turning off circulation_pump")
            self.circulation_pump = False

    def turn_on_jet_pump_one(self):
        if self.jet_pump_one:
            print("jet_pump_one was already on")
        else:
            print("turning on jet_pump_one")
            self.jet_pump_one = True

    def turn_off_jet_pump_one(self):
        if not self.jet_pump_one:
            print("jet_pump_one was already off")
        else:
            print("turning off jet_pump_one")
            self.jet_pump_one = False

    def turn_on_jet_pump_two(self):
        if self.jet_pump_two:
            print("jet_pump_two was already on")
        else:
            print("turning on jet_pump_two")
            self.jet_pump_two = True

    def turn_off_jet_pump_two(self):
        if not self.jet_pump_two:
            print("jet_pump_two was already off")
        else:
            print("turning off jet_pump_two")
            self.jet_pump_two = False

    def turn_on_blower(self):
        if self.blower:
            print("blower was already on")
        else:
            print("turning on blower")
            self.blower = True

    def turn_off_blower(self):
        if not self.blower:
            print("blower was already off")
        else:
            print("turning off blower")
            self.blower = False

    def turn_on_heater(self):
        if self.heater:
            print("heater was already on")
        elif self.can_turn_on_heat():
            print("turning on heater")
            self.heater = True
        else:
            print("Error: cannot turn on heater!")

    def turn_off_heater(self):
        if not self.heater:
            print("heater was already off")
        else:
            print("turning off heater")
            self.heater = False
