from machine import Pin
import machine
from time import sleep
import esp32
print(esp32.hall_sensor())     
print(esp32.raw_temperature()) 
led = Pin(2,Pin.OUT)
machine.freq(240000000)
print(machine.freq())
while True:
    led.on()
    sleep(2)
    led.off()
    sleep(2)
