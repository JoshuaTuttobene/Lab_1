
import micropython
import utime
"""! @file led.py
Doxygen style docstring for the file (change this!)"""

def led_setup ():
    """! Doxygen style docstring for this function """
    pinA0 = pyb.Pin(pyb.Pin.board.PA0, pyb.Pin.OUT_PP)
    tim2 = pyb.Timer(2, freq=1)
    ch1 = tim2.channel(1, pyb.Timer.PWM_INVERTED, pin=pinA0)
    return ch1

def led_brightness (x,ch):
    
    """! Doxygen style docstring for this function """
    ch.pulse_width_percent(x)

ch1 = led_setup()
while True:
    led_brightness(50, ch1)
        
    
