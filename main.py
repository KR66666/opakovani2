from machine import Pin
from time import sleep
import dht 
import machine
import time

sensor = dht.DHT11(Pin(0))
button = machine.Pin(1, machine.Pin.IN, machine.Pin.PULL_UP)

stavT = 1  
stavH = 0  

while True:
    try:
        sleep(0.5)
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()

        if button.value() == 1:   
            if stavT == 1:
                stavT = 0 
                stavH = 1
            else:
                stavT = 1 
                stavH = 0

        if stavT == 1:
            print('Temperature: %3.1f C' % temp)
        if stavH == 1:
            print('Humidity: %3.1f %%' % hum)

    except OSError as e:
        print('Failed to read sensor.')