#!/usr/bin/env python3
from temperature import Temperature
#             print('self.heater = {}'.format(self.heater))


class InOut:
    def __init__(self):
        self.temp = Temperature()
        self.elements = {
            'circulation_pump': False,
            'jet_pump_one': False,
            'jet_pump_two': False,
            'blower': False,
            'heater': False
        }

    def on(self, key):
        status = self.elements[key]
        # print('{} was {}'.format(key, status))
        return status

    def turn_on(self, key):
        print('turning on {}'.format(key))
        self.elements[key] = True

    def turn_off(self, key):
        print('turning off {}'.format(key))
        self.elements[key] = False

    @staticmethod
    def air_temp():
        return 76

    @staticmethod
    def water_temp():
        return 104

    @staticmethod
    def max_temp():
        return 106

    @staticmethod
    def flowing():
        return True

    def can_turn_on_heat(self):
        return self.flowing() and self.water_temp() <= self.max_temp()

    def turn_on_circulation_pump(self):
        if not self.on('circulation_pump'):
            self.turn_on('circulation_pump')

    def turn_off_circulation_pump(self):
        if self.on('circulation_pump'):
            self.turn_off('circulation_pump')

    def turn_on_jet_pump_one(self):
        if not self.on('jet_pump_one'):
            self.turn_on('jet_pump_one')

    def turn_off_jet_pump_one(self):
        if self.on('jet_pump_one'):
            self.turn_off('jet_pump_one')

    def turn_on_jet_pump_two(self):
        if not self.on('jet_pump_two'):
            self.turn_on('jet_pump_two')

    def turn_off_jet_pump_two(self):
        if self.on('jet_pump_two'):
            self.turn_off('jet_pump_two')

    def turn_on_blower(self):
        if not self.on('blower'):
            self.turn_on('blower')

    def turn_off_blower(self):
        if self.on('blower'):
            self.turn_off('blower')

    def turn_on_heater(self):
        if not self.on('heater'):
            if self.can_turn_on_heat():
                self.turn_on('heater')
            else:
                print('Error: cannot turn on heater!')

    def turn_off_heater(self):
        if self.on('heater'):
            self.turn_off('heater')

