from machine import Pin, I2C
import ssd1306
from time import sleep


i2c = I2C(-1, scl=Pin(22), sda=Pin(21))
 
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

oled.text('Welcome to Lab!', 0, 0)
oled.text('Ashraf 20184792', 0, 16)
oled.text('Youssef 20184117', 0, 32)
        
oled.show()