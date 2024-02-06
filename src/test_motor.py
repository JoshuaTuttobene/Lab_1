import micropython
import pyb
import motor_driver as MD

# Test out if code calls class
if __name__ == "__main__":
    
    encoder_pin = pyb.Pin(pyb.Pin.board.PA10, pyb.Pin.OUT_PP)
    in1pin = pyb.Pin.cpu.B4
    in2pin = pyb.Pin.cpu.B5
    tim3 = pyb.Timer(3, freq=20000)
    motor = MD.MotorDriver(encoder_pin, in1pin, in2pin, tim3)
    motor.enable()
    while True:
        user = input()
        motor.set_duty_cycle(user)
