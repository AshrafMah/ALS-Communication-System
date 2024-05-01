from machine import Pin, I2C ,ADC ,deepsleep
from time import sleep,time
from mpu import Accel
import ssd1306
import esp32

i2c = I2C(scl=Pin(22), sda=Pin(21)) 
mpu= Accel(i2c)

while True:
    value = mpu.get_values()
    y = value["AcY"]
    x = value["AcX"]
    z = value["AcZ"]
    
    if y < 0 and x > 8000 :
        print("right")
    
    elif x < 0 and z > 0:
        print("left")
    elif y < 0 and x < 7000 and z < 7000:
        print("back")
    elif y > 7000 and x < 7000 and z < 7000:
        print("forward")
    
    else:
        print("stop")
        
    sleep(1.5)
    print(value)