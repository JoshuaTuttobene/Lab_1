
import micropython
import utime

class MotorDriver:
    """! 
    This class implements a motor driver for an ME405 kit. 
    """

    def __init__ (self, en_pin, in1pin, in2pin, timer):
        """! 
        Creates a motor driver by initializing GPIO
        pins and turning off the motor for safety. 
        @param en_pin (There will be several parameters)
        """
        print ("Creating a motor driver")
        
        pin_ENA = pyb.Pin(pyb.Pin.board.PINA10, pyb.Pin.OUT_PP)
        
        pin1A = pyb.Pin(pyb.Pin.board.PB4, pyb.Pin.OUT_PP)
        tim3 = pyb.Timer(3, freq=500)
        ch1 = tim3.channel(1, pyb.Timer.PWM, pin=pin1A)
        
        pin2A = pyb.Pin(pyb.Pin.board.PB5, pyb.Pin.OUT_PP)
        tim3 = pyb.Timer(3, freq=500)
        ch2 = tim3.channel(2, pyb.Timer.PWM, pin=pin2A)
        
        return ch1, ch2

    def set_duty_cycle (self, level):
        """!
        This method sets the duty cycle to be sent
        to the motor to the given level. Positive values
        cause torque in one direction, negative values
        in the opposite direction.
        @param level A signed integer holding the duty
               cycle of the voltage sent to the motor 
        """
        print (f"Setting duty cycle to {level}")

        ch.pulse_width_percent(x)
        
    ch1, ch2 = __init__(self, pin_ENA, pin1A, pin2A, timer)

    while True:
        set_duty_cycle(self, 50)
    
