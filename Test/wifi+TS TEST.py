import machine
import urequests 
from machine import Pin, SoftI2C , ADC
import network, time

from time import sleep



HTTP_HEADERS = {'Content-Type': 'application/json'} 
THINGSPEAK_WRITE_API_KEY = '7UKLHPE2R62DOTXJ' 

UPDATE_TIME_INTERVAL = 5000  # in ms 
last_update = time.ticks_ms() 

ssid='AM'
password='941999*#'

# Configure ESP32 as Station
sta_if=network.WLAN(network.STA_IF)
sta_if.active(True)

if not sta_if.isconnected():
    print('connecting to network...')
    sta_if.connect(ssid, password)
    while not sta_if.isconnected():
     pass
print('network config:', sta_if.ifconfig()) 

while True: 
    if time.ticks_ms() - last_update >= UPDATE_TIME_INTERVAL:
        
        ldr=ADC(Pin(35))
        ldr.atten(ADC.ATTN_11DB)
        x=ldr.read()

        bme_readings = {'field1':x} 
        request = urequests.post( 'http://api.thingspeak.com/update?api_key=' + THINGSPEAK_WRITE_API_KEY, json = bme_readings, headers = HTTP_HEADERS )  
        request.close() 
        print(bme_readings) 