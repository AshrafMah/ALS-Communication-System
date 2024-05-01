from machine import Pin, I2C ,ADC
from time import sleep
from mpu import Accel
import ssd1306

#For the led , buzzer & LDR
led = Pin(5 , Pin.OUT)
buzzer= Pin(18 , Pin.OUT)
ldr= ADC(Pin(35))
ldr.atten(ADC.ATTN_11DB)

#For the joystick
X = ADC(Pin(32, Pin.IN))
Y = ADC(Pin(33, Pin.IN))
X.atten(ADC.ATTN_11DB)
Y.atten(ADC.ATTN_11DB)

#For the dislpay &accelometer 
i2c = I2C(scl=Pin(22), sda=Pin(21)) 
mpu= Accel(i2c)

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)


while True:
    ldr_value=ldr.read()
    print('value = {}'.format(ldr_value))
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
        buzzer.on()
        
    else:
        oled.fill(0)
        print("stop")
        
    sleep(0.5)
    print(value)
     
    
    
    while True:
        
        xx = X.read()
        yy = Y.read()
        
        if yy==4095 and 4095 > xx  :
           print("right")
           oled.fill(0)
           oled.text('Yes', 50, 32)
           oled.show()
       
        
        elif  xx < 4095 and yy==0 :
            print("left")
            oled.fill(0)
            oled.text('No', 50, 32)
            oled.show()
         
        elif  yy < 4095 and xx==0 :
            print("back")
            oled.fill(0)
            oled.text('IDK', 50, 32)
            oled.show()
        
        elif xx==4095 and 4095 > yy:
            print("forward")
            oled.fill(0)
            oled.text('Thanks', 50, 32)
            oled.show()
        
        else:
            print("stop")
            oled.fill(0)
            
           
        break
    sleep(0.2)

    
    
