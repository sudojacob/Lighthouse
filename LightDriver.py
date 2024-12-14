from picozero import Button
from picozero import LED
import machine
import utime

button = machine.Pin(18, machine.Pin.IN, machine.Pin.PULL_UP)

led = LED(25)

def off():
    led.off()

def on():
    led.on()
        
def blink():
    led.on()
    utime.sleep(.2)
    led.off()
    utime.sleep(.2)

NUM_OPTIONS = 3
setting = 0 # store the current option
last_time = 0
print("setting: ", setting)
def handleClick(p):
    global last_time
    new_time = utime.ticks_ms()
    # if it has been more that 1/5 of a second since the last event, we have a new event
    if (new_time - last_time) < 300: 
        return
    last_time = new_time
    global setting
    setting = (setting + 1) % NUM_OPTIONS
    print("new setting: ", setting)
    

button.irq(trigger=machine.Pin.IRQ_FALLING, handler=handleClick)

while True:
    if setting is 0:
        off()
    elif setting is 1:
        on()
    elif setting is 2:
        blink()
