import time
from neopixel import Neopixel
import colors

class Lighthouse:
    def __init__(self):
        # Initialize Neopixels
        # =======================================
        print("Initializing neopixels")
        # TOP LIGHT
        numpix_top = 32
        self.top_light = Neopixel(numpix_top, 0, 6, "WRGB")
        self.top_light.brightness(100)
        self.top_light.fill(colors.STARTUP)
        self.top_light.show()
        time.sleep(.5)
        self.top_light.fill(colors.OFF)
        self.top_light.show()
        time.sleep(.5)
        
        # INTERIOR LIGHTS
        numpix_interior = 3
        self.interior_lights = Neopixel(numpix_interior, 0, 28, "GRB")
        self.interior_lights.brightness(100)
        self.interior_lights.fill(colors.INTERIOR_STARTUP)
        self.interior_lights.show()
        time.sleep(.5)
        self.interior_lights.fill(colors.INTERIOR_OFF)
        self.interior_lights.show()
        time.sleep(.5)
        # =========================================
        
        # state 0: off
        # state 1: low brightness
        # state 2: medium brightness
        # state 3: full brightness
        # state 4: rotating beam
        self.state = 0
        self.prev_run = 0
    
    def state_0(self):
        print("State 0: Off")
        numpix_top = 32
        self.top_light = Neopixel(numpix_top, 0, 6, "WRGB")
        self.top_light.fill(colors.TOP_LEVEL_0)
        self.top_light.show()
        
        numpix_interior = 3
        self.interior_lights = Neopixel(numpix_interior, 0, 28, "GRB")
        self.interior_lights.fill(colors.INTERIOR_LEVEL_0)
        self.interior_lights.show()
        
    def state_1(self):
        print("State 1: Low Brightness")
        numpix_top = 32
        self.top_light = Neopixel(numpix_top, 0, 6, "WRGB")
        self.top_light.fill(colors.TOP_LEVEL_1)
        self.top_light.show()
        
        numpix_interior = 3
        self.interior_lights = Neopixel(numpix_interior, 0, 28, "GRB")
        self.interior_lights.fill(colors.INTERIOR_LEVEL_1)
        self.interior_lights.show()
    
    def state_2(self):
        print("State 2: Medium Brightness")
        numpix_top = 32
        self.top_light = Neopixel(numpix_top, 0, 6, "WRGB")
        self.top_light.fill(colors.TOP_LEVEL_2)
        self.top_light.show()
        
        numpix_interior = 3
        self.interior_lights = Neopixel(numpix_interior, 0, 28, "GRB")
        self.interior_lights.fill(colors.INTERIOR_LEVEL_2)
        self.interior_lights.show()
    
    def state_3(self):
        print("State 3: High Brightness")
        numpix_top = 32
        self.top_light = Neopixel(numpix_top, 0, 6, "WRGB")
        self.top_light.fill(colors.TOP_LEVEL_3)
        self.top_light.show()
        
        numpix_interior = 3
        self.interior_lights = Neopixel(numpix_interior, 0, 28, "GRB")
        self.interior_lights.fill(colors.INTERIOR_LEVEL_3)
        self.interior_lights.show()
    
    def light_ring_pos(self, n, color):
        top = 16 - n
        top += 10
        top = top % 16
        self.top_light.set_pixel(n, color)
        self.top_light.set_pixel(top + 16, color)
        
    
    def state_4(self):
        print("State 4: Rotating Beam")
        numpix_interior = 3
        self.interior_lights = Neopixel(numpix_interior, 0, 28, "GRB")
        self.interior_lights.fill(colors.INTERIOR_LEVEL_3)
        self.interior_lights.show()
        time.sleep(.5)
        
        numpix_top = 32
        self.top_light = Neopixel(numpix_top, 0, 6, "WRGB")
        
        ring_pixel = 0
        
        self.light_ring_pos(ring_pixel, colors.BEAM)
        self.light_ring_pos(ring_pixel + 1, colors.BEAM)
        self.light_ring_pos(ring_pixel + 2, colors.BEAM)
        self.light_ring_pos(ring_pixel + 3, colors.BEAM)
        self.top_light.show()
        while self.state == 4:
            self.light_ring_pos(ring_pixel, colors.OFF)
            ring_pixel = (ring_pixel + 1) % 16
            self.light_ring_pos((ring_pixel + 3) % 16, colors.BEAM)
            self.top_light.show()
            time.sleep(.1)
        
    
    def run(self):
        if self.state == self.prev_run:
            return
        self.prev_run = self.state
        
        
        if self.state == 0:
            self.state_0()
        elif self.state == 1:
            self.state_1()
        elif self.state == 2:
            self.state_2()
        elif self.state == 3:
            self.state_3()
        elif self.state == 4:
            self.state_4()
    

    def handler(self, change):
        self.state = (self.state + 1) % 5
        print("Button pressed; new state: ", self.state)
