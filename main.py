import time
from neopixel import Neopixel
from machine import Pin, Timer
from lighthouse import Lighthouse

lighthouse = Lighthouse()

def debounce(pin):
    # Start or replace a timer for 200ms, and trigger on_pressed.
    timer.init(mode=Timer.ONE_SHOT, period=500, callback=lighthouse.handler)

# Register a new hardware timer.
timer = Timer(-1)

button = Pin(18, Pin.IN, Pin.PULL_UP)
button.irq(handler=debounce, trigger=Pin.IRQ_FALLING)

while True:
    lighthouse.run()
    time.sleep(1)
