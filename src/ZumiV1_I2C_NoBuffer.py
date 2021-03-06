#this program reads the serial port
#at a baud rate of 115200
#This code works with Linky

import smbus
import time

bus = smbus.SMBus(1)
address = 0x04

def forward():
    bus.write_byte(address, 77)

def backward():
    bus.write_byte(address, 78)

def left():
    bus.write_byte(address, 79)

def right():
    bus.write_byte(address, 80)

def stop():
    bus.write_byte(address, 81)

def setMotor(i, j):
    """Sets the individual speed of each motor.
    Args: 2 integers, from -100 to 100, for the left and right motors, respectively.
    """
    if i<0:
        i=-i
        if j<0:
            a = 67
            j=-j
        else:
            a = 66
    else:
        if j<0:
            a = 65
            j=-j
        else:
            a = 64
    if i>100:
        i = 100
    if j>100:
        j = 100
    bus.write_i2c_block_data(address, a, [int(i), int(j)])

def setSpeed(i):
    if i < 0:
        i = 0
    if i > 100:
        i = 100
    bus.write_byte_data(address, 70, int(i))

def turnDegrees(i):
    a=69
    if i < 0:
        i=-i
        a=68
    if i > 180:
        i = 180
    bus.write_byte_data(address, a, int(i))

def waitUntilTurnDegrees():
    while bus.read_byte(address) == 1:
        time.sleep(1)
