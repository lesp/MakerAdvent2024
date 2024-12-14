from machine import Pin, PWM
from time import sleep

# Set up PWM Pin for servo control
servo_pin = machine.Pin(16)
pir_pin = 17
servo = PWM(servo_pin)
pir = Pin(pir_pin, Pin.IN)

# Set Duty Cycle for Different Angles
max_duty = 7864
min_duty = 1802
half_duty = int(max_duty/2)

#Set PWM frequency
frequency = 50
servo.freq (frequency)

while True:
    if pir.value() == 1:  # Motion detected
        servo.duty_u16(half_duty)
        sleep(0.1)
    else:
    #Servo at 0 degrees
        servo.duty_u16(max_duty)
        sleep(0.1)
