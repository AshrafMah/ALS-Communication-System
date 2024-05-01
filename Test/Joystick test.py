from machine import Pin, ADC
from time import sleep_ms

x = ADC(Pin(32, Pin.IN))
y = ADC(Pin(33, Pin.IN))
x.atten(ADC.ATTN_11DB)
y.atten(ADC.ATTN_11DB)

while True:
    x_val = x.read()
    y_val = y.read()
    print('Current position:{},{}'.format(x_val,y_val))
    sleep_ms(300)