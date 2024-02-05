
import micropython
import utime
class MotorDriver:
    """! 
    This class implements a motor driver for an ME405 kit. 
    """

    def __init__ (self):
        """! 
        Creates a motor driver by initializing GPIO
        pins and turning off the motor for safety. 
        @param en_pin (There will be several parameters)
        """
        pin_ENA = pyb.Pin(pyb.Pin.cpu.A10, pyb.Pin.OUT_PP)
        
        pin1A = pyb.Pin.cpu.B4
        tim3 = pyb.Timer(3, freq=20000)
        ch1 = tim3.channel(1, pyb.Timer.PWM, pin=pin1A)
        
        pin2A = pyb.Pin.cpu.B5
        tim3 = pyb.Timer(3, freq=20000)
        ch2 = tim3.channel(2, pyb.Timer.PWM, pin=pin2A)
        
        pin_ENA.high()
        
        self.ch1 = ch1
        self.ch2 = ch2
        
        print ("Creating a motor driver")

    def set_duty_cycle (self,level1,level2):
        """!
        This method sets the duty cycle to be sent
        to the motor to the given level. Positive values
        cause torque in one direction, negative values
        in the opposite direction.
        @param level A signed integer holding the duty
               cycle of the voltage sent to the motor 
        """
        print (f"Setting duty cycle to {level1}")
        self.ch1.pulse_width_percent(level1)
        self.ch2.pulse_width_percent(level2)
        
motor = MotorDriver()
motor.set_duty_cycle(100,0)