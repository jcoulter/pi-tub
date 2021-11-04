#!/usr/bin/env python3
# import RPi.GPIO as GPIO
from input_output import InOut
from flask import Flask, render_template
from flask import request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    in_out = InOut()
    water_temperature = in_out.water_temp()
    air_temperature = in_out.air_temp()
    flowing = in_out.flowing()
    print("The water temperature is {}".format(water_temperature))

    circulation_pump = request.form.get('circulation_pump')
    jet_pump_one = request.form.get('jet_pump_one')
    jet_pump_two = request.form.get('jet_pump_two')
    blower = request.form.get('blower')
    heater = request.form.get('heater')

    if request.method == 'POST':
        print("I am posting!")
        # print initial pin status before evaluating and changing
        # circulation_pump = request.form.get('circulation_pump')
        if circulation_pump == 'on':
            in_out.turn_on_circulation_pump()
        else:
            in_out.turn_off_circulation_pump()

        if jet_pump_one == 'on':
            in_out.turn_on_jet_pump_one()
        else:
            in_out.turn_off_jet_pump_one()

        if jet_pump_two == 'on':
            in_out.turn_on_jet_pump_two()
        else:
            in_out.turn_off_jet_pump_two()

        if blower == 'on':
            in_out.turn_on_blower()
        else:
            in_out.turn_off_blower()

        if heater == 'on':
            in_out.turn_on_heater()
        else:
            in_out.turn_off_heater()

    if request.method == 'GET':
        print("I am getting!!")

    return render_template("status.html", flowing=flowing, water_temperature=water_temperature,
                           air_temperature=air_temperature, circulation_pump=circulation_pump,
                           jet_pump_one=jet_pump_one, jet_pump_two=jet_pump_two, blower=blower, heater=heater)
