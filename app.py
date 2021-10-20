#!/usr/bin/env python3
import RPi.GPIO as GPIO
from flask import Flask, render_template
from flask import request

app = Flask(__name__)


# def setupGPIO():
# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)
#
# GPIO.setup(18, GPIO.OUT)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    # setupGPIO()
    # TODO: make the devices properties
    temp_store1 = open(
        "/sys/bus/w1/devices/28-012063bee088/w1_slave")  # change this number to the Device ID of your sensor
    raw_water = temp_store1.read()
    temp_store1.close()
    water_temperature = float(raw_water.split("\n")[1].split(" ")[9][2:])
    water_temperature = water_temperature / 1000
    # Fahrenheit = (Celsius * 9 / 5) + 32
    print("The water temperature is {}".format(water_temperature))

    # TODO: make the devices properties
    temp_store2 = open(
        "/sys/bus/w1/devices/28-012063c43c9d/w1_slave")  # change this number to the Device ID of your sensor
    raw_air = temp_store2.read()
    temp_store2.close()
    air_temperature = float(raw_air.split("\n")[1].split(" ")[9][2:])
    air_temperature = air_temperature / 1000
    # Fahrenheit = (Celsius * 9 / 5) + 32
    print("The air temperature is {}".format(air_temperature))

    if request.method == 'POST':
        print("I am posting!")
        # print initial pin status before evaluating and changing
        circulation_pump = request.form.get('circulation_pump')
        if circulation_pump == 'On':
            print("I am on!")
        #     GPIO.output(18, GPIO.HIGH)
        else:
            print("I am on!")
        #     GPIO.output(18, GPIO.LOW)

        print("Circulation Pump is {}".format(circulation_pump))
    if request.method == 'GET':
        print("I am getting!!")

    return render_template("status.html")
