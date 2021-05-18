import RPi.GPIO as GPIO
import spidev
from time import sleep

# location, timestamp, data
# Shashank needs sample data sets

# Initialisiere Licht-Sensor auf Analogen-PIN 0
temp = 4

spi = spidev.SpiDev()
spi.open(0, 0)


def readadc(adcnum):
    # SPI-Daten auslesen
    r = spi.xfer2([1, 8 + adcnum << 4, 0])
    adcout = ((r[1] & 3) << 8) + r[2]
    return adcout


while True:
    value = readadc(temp)
    print("Value: " + str(value))
