from machine import Pin, I2C ,ADC
from time import sleep
from mpu import Accel
import ssd1306

led = Pin(5 , Pin.OUT)
buzzer= Pin(18 , Pin.OUT)
ldr= ADC(Pin(34))
ldr.atten(ADC.ATTN_11DB)

i2c = I2C(scl=Pin(22), sda=Pin(21)) 
mpu= Accel(i2c)


oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

while True:
    ldr_value=ldr.read()
    value = mpu.get_values()
    y = value["AcY"]
    x = value["AcX"]
    z = value["AcZ"]
    oled.invert(True)
    
    if(ldr_value < 1000):
        led.on()
        buzzer.on()
    
    else:
        led.off()
        buzzer.off()
    sleep(0.5)
    
    if y < 0 and x > 8000 :
        print("right")
        oled.fill(0)
        oled.text('Eat', 50, 32)
        oled.show()
    
    elif x < 0 and z > 0:
        print("left")
        oled.fill(0)
        oled.text('Sleep', 50, 32)
        oled.show()
    elif y < 0 and x < 7000 and z < 7000:
        print("back")
        oled.fill(0)
        oled.text('toilet', 50, 32)
        oled.show()
    elif y > 7000 and x < 7000 and z < 7000:
        print("forward")
        oled.fill(0)
        oled.text('tired', 50, 32)
        oled.show()
        
    else:
        oled.fill(0)
        print("stop")
        oled.text('MOVE TO WORK!', 15, 32)
        oled.show()
    sleep(1.5)
    print(value)