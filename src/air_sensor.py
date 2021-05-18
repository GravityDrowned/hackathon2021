#!/usr/bin/env python

import bme680
import board
from busio import I2C
import adafruit_bme680 as af_bme680
import time


def read_air_data():
    # ToDo: value checks
    ex_gas = None
    ex_humidity = None
    ex_air_quality_score = None
    ex_temperature = None
    ex_pressure = None
    ex_altitude = None

    if sensor.get_sensor_data():
        '''
        print("altitude:", af_bme680.altitude)
        output = '{0:.2f} C,{1:.2f} hPa,{2:.2f} %RH'.format(
            '''
        ex_temperature = sensor.data.temperature
        ex_pressure = sensor.data.pressure
        ex_humidity = sensor.data.humidity

        if sensor.data.heat_stable:
            gas = sensor.data.gas_resistance
            gas_offset = gas_baseline - gas

            hum = sensor.data.humidity
            hum_offset = hum - hum_baseline

            # Calculate hum_score as the distance from the hum_baseline.
            if hum_offset > 0:
                hum_score = (100 - hum_baseline - hum_offset)
                hum_score /= (100 - hum_baseline)
                hum_score *= (hum_weighting * 100)

            else:
                hum_score = (hum_baseline + hum_offset)
                hum_score /= hum_baseline
                hum_score *= (hum_weighting * 100)

            # Calculate gas_score as the distance from the gas_baseline.
            if gas_offset > 0:
                gas_score = (gas / gas_baseline)
                gas_score *= (100 - (hum_weighting * 100))

            else:
                gas_score = 100 - (hum_weighting * 100)

            # Calculate air_quality_score.
            air_quality_score = hum_score + gas_score
            ex_air_quality_score = air_quality_score
            '''
            print(air_quality_score)

            print('Gas: {0:.2f} Ohms,humidity: {1:.2f} %RH,air quality: {2:.2f}'.format(
                gas,
                hum,
                air_quality_score))
            '''
        '''
        if sensor.data.heat_stable:
            print('{0},{1} %'.format(
                output,
                air_quality_score))

        else:
            print(output)
        '''
        return ex_gas, ex_humidity, ex_air_quality_score, ex_temperature, ex_pressure, ex_altitude


def config_new_gas_baseline():
    '''
    # Collect gas resistance burn-in values, then use the average
    # of the last 50 values to set the upper limit for calculating
    # gas_baseline.
    :return: new gase baseline value
    '''
    start_time = time.time()
    curr_time = time.time()
    burn_in_time = 300

    burn_in_data = []

    print('Collecting gas resistance burn-in data for 5 mins\n')
    while curr_time - start_time < burn_in_time:
        curr_time = time.time()
        if sensor.get_sensor_data() and sensor.data.heat_stable:
            gas = sensor.data.gas_resistance
            burn_in_data.append(gas)
            print('Gas: {0} Ohms'.format(gas))
            time.sleep(1)

    gas_baseline = sum(burn_in_data[-50:]) / 50.0

    return gas_baseline


print("""read-all.py - Displays temperature, pressure, humidity, and gas.

Press Ctrl+C to exit!

""")

# Create library object using our Bus I2C port
i2c = I2C(board.SCL, board.SDA)
af_bme680 = af_bme680.Adafruit_BME680_I2C(i2c, debug=False)
# change this to match the location's pressure (hPa) at sea level
af_bme680.sea_level_pressure = 1013.25

try:
    sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
except (RuntimeError, IOError):
    sensor = bme680.BME680(bme680.I2C_ADDR_SECONDARY)

# These calibration data can safely be commented
# out, if desired.

print('Calibration data:')
for name in dir(sensor.calibration_data):

    if not name.startswith('_'):
        value = getattr(sensor.calibration_data, name)

        if isinstance(value, int):
            print('{}: {}'.format(name, value))

# These oversampling settings can be tweaked to
# change the balance between accuracy and noise in
# the data.

sensor.set_humidity_oversample(bme680.OS_2X)
sensor.set_pressure_oversample(bme680.OS_4X)
sensor.set_temperature_oversample(bme680.OS_8X)
sensor.set_filter(bme680.FILTER_SIZE_3)
sensor.set_gas_status(bme680.ENABLE_GAS_MEAS)

# Set the gas base_line to Michaels room
gas_baseline = 683113.0155294954

# Set the humidity baseline to 40%, an optimal indoor humidity.
hum_baseline = 40.0

# This sets the balance between humidity and gas reading in the
# calculation of air_quality_score (25:75, humidity:gas)
hum_weighting = 0.25

print('Gas baseline: {0} Ohms, humidity baseline: {1:.2f} %RH\n'.format(
    gas_baseline,
    hum_baseline))

print('\n\nInitial reading:')
for name in dir(sensor.data):
    value = getattr(sensor.data, name)

    if not name.startswith('_'):
        print('{}: {}'.format(name, value))

sensor.set_gas_heater_temperature(320)
sensor.set_gas_heater_duration(150)
sensor.select_gas_heater_profile(0)

# Up to 10 heater profiles can be configured, each
# with their own temperature and duration.
# sensor.set_gas_heater_profile(200, 150, nb_profile=1)
# sensor.select_gas_heater_profile(1)

print('\n\nPolling:')
try:
    while True:
        ex_gas, ex_humidity, ex_air_quality_score, ex_temperature, ex_pressure, ex_altitude = read_air_data()
        print(ex_gas, ex_humidity, ex_air_quality_score, ex_temperature, ex_pressure, ex_altitude)
        time.sleep(1)

except KeyboardInterrupt:
    pass
