
import micropython
import utime
"""! @file led.py
Doxygen style docstring for the file (change this!)"""

def led_setup ():
    """! Doxygen style docstring for this function """
    pinA0 = pyb.Pin(pyb.Pin.board.PA0, pyb.Pin.OUT_PP)
    pinA0.high()
    pinA0.low()

def led_brightness ():
    """! Doxygen style docstring for this function """
    More function code here

if __name__ == "__main__":
    # PWM
    while True:
        pinA0.value(0)
        # utime.sleep(2)
        pinA0.value(1)
        # utime.sleep(2)
    
