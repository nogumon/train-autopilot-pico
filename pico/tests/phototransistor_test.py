from machine import ADC
import time

adc = ADC(26)  # GP26

while True:
    value = adc.read_u16()
    print(value)
    time.sleep(0.2)
 