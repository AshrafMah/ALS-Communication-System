from machine import Pin , ADC
from time import sleep

led = Pin(5 , Pin.OUT)
buzzer= Pin(18 , Pin.OUT)
ldr= ADC(Pin(35))
ldr.atten(ADC.ATTN_11DB)

         
while True:
 ldr_value=ldr.read()
 print('value = {}'.format(ldr_value))
    
 if(ldr_value < 1000):
    led.on()
    buzzer.on()
  
 else:
    led.off()
    buzzer.off()  
    sleep(0.5)