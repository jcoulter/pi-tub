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

    # TODO: make the devices properties

    print("The air temperature is {}".format(air_temperature))

    if request.method == 'POST':
        print("I am posting!")
        # print initial pin status before evaluating and changing
        circulation_pump = request.form.get('circulation_pump')
        if circulation_pump == 'On':
            print("I am on!")
        #     GPIO.output(18, GPIO.HIGH)
        else:
            print("I am off!")
        #     GPIO.output(18, GPIO.LOW)

        print("Circulation Pump is {}".format(circulation_pump))
    if request.method == 'GET':
        print("I am getting!!")

    return render_template("status.html", water_temperature=water_temperature, air_temperature=air_temperature, circulation_pump=circulation_pump)
