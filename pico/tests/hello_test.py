from machine import Pin
import time

led = Pin("LED", Pin.OUT)

print("hello test start")

for i in range(10):
    led.toggle()
    print("tick", i)
    time.sleep(0.2)

print("done")
