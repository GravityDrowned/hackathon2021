
'''
In our example of how to convert the BME680's gas resistance readings into a percentage indoor air quality (IAQ),
we took a background reading for 5 minutes, then set this as the optimal gas resistance reading (100%), and also
factored in humidity with a weighting of 75:25 for gas:humidity, as humidity also has an effect on IAQ (a relative humidity of 40% is optimal).

Gas baseline: 683113.0155294954 Ohms, humidity baseline: 40.00 %RH

'''
import time
import board
from busio import I2C
#import adafruit_bme680
import bme680



#Gas baseline: 683113.0155294954 Ohms, humidity baseline: 40.00 %RH
gas_baseline = 683113.0155294954
# Set the humidity baseline to 40%, an optimal indoor humidity.
hum_baseline = 40.0
# This sets the balance between humidity and gas reading in the
# calculation of air_quality_score (25:75, humidity:gas)
hum_weighting = 0.25
# Create library object using our Bus I2C port
i2c = I2C(board.SCL, board.SDA)

#bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c, debug=False)
try:
    sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
except (RuntimeError, IOError):
    sensor = bme680.BME680(bme680.I2C_ADDR_SECONDARY)

# change this to match the location's pressure (hPa) at sea level
sensor.sea_level_pressure = 1013.25
while True:
    print("\nTemperature: %0.1f C" % bme680.temperature)
    print("Gas: %d ohm" % bme680.gas)
    print("Humidity: %0.1f %%" % bme680.humidity)
    print("Pressure: %0.3f hPa" % bme680.pressure)
    print("Altitude = %0.2f meters" % bme680.altitude)

    try:
        sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
    except (RuntimeError, IOError):
        sensor = bme680.BME680(bme680.I2C_ADDR_SECONDARY)

    if sensor.get_sensor_data() and sensor.data.heat_stable:
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

    time.sleep(1)