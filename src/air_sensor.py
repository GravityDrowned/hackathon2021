# https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-bme680-breakout

'''
In our example of how to convert the BME680's gas resistance readings into a percentage indoor air quality (IAQ),
we took a background reading for 5 minutes, then set this as the optimal gas resistance reading (100%), and also
factored in humidity with a weighting of 75:25 for gas:humidity, as humidity also has an effect on IAQ (a relative humidity of 40% is optimal).

Gas baseline: 683113.0155294954 Ohms, humidity baseline: 40.00 %RH



'''
'''
import time
import board
from busio import I2C
import adafruit_bme680


# Create library object using our Bus I2C port
i2c = I2C(board.SCL, board.SDA)
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c, debug=False)
# change this to match the location's pressure (hPa) at sea level
bme680.sea_level_pressure = 1013.25
while True:
    print("\nTemperature: %0.1f C" % bme680.temperature)
    print("Gas: %d ohm" % bme680.gas)
    print("Humidity: %0.1f %%" % bme680.humidity)
    print("Pressure: %0.3f hPa" % bme680.pressure)
    print("Altitude = %0.2f meters" % bme680.altitude)
    time.sleep(1)
'''

import time
import bme680


try:
    sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
except (RuntimeError, IOError):
    sensor = bme680.BME680(bme680.I2C_ADDR_SECONDARY)

# These oversampling settings can be tweaked to
# change the balance between accuracy and noise in
# the data.

bme680.sea_level_pressure = 1013.25
sensor.set_humidity_oversample(bme680.OS_2X)
sensor.set_pressure_oversample(bme680.OS_4X)
sensor.set_temperature_oversample(bme680.OS_8X)
sensor.set_filter(bme680.FILTER_SIZE_3)

print('Polling:')
try:
    while True:
        if sensor.get_sensor_data():
            print("\nTemperature: %0.1f C" % bme680.temperature)
            print("Gas: %d ohm" % bme680.gas)
            print("Humidity: %0.1f %%" % bme680.humidity)
            print("Pressure: %0.3f hPa" % bme680.pressure)
            print("Altitude = %0.2f meters" % bme680.altitude)
            time.sleep(1)

except KeyboardInterrupt:
    pass
