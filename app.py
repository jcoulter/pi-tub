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
        if jet_pump_one == 'on':
            print("jet_pump_one is on!")
        #     GPIO.output(18, GPIO.HIGH)
        else:
            print("jet_pump_one is off!")
        #     GPIO.output(18, GPIO.LOW)

        print("Circulation Pump is {}".format(circulation_pump))
        print("Jet Pump One is {}".format(jet_pump_one))
        print("Jet Pump Two is {}".format(jet_pump_two))
        print("Blower is {}".format(blower))
        print("Heater is {}".format(heater))
    if request.method == 'GET':
        print("I am getting!!")

    return render_template("status.html", water_temperature=water_temperature, air_temperature=air_temperature, circulation_pump=circulation_pump, jet_pump_one=jet_pump_one, jet_pump_two=jet_pump_two, blower=blower, heater=heater)
