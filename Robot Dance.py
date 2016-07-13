#David & Vicente
#Robot Dance.py
#The robot dance.

#first, initialize the scribbler.
from Myro import *
init("COM9")
#define functions needed:

#shake: movement of left to right or right to left, depending on first argument - direction.
#three arguments must be passed: direction, seconds(duration), speed.
def shake(dire,sec,sp):
    #checks direction. 'l' means left
    if dire == "l":
        turnLeft(sec,sp)
        turnRight(sec,sp)
    #if its not left, it must be right.
    else:
        turnRight(sec,sp)
        turnLeft(sec,sp)

#movement of in and out. Will go forward and backward
def inOut(sec,sp):
    forward(sec,sp)
    backward(sec,sp)

#the whole dance.
def dance():
    for i in range(1,5):
        rotate(4,2.55)
        inOut(2,1)
        for j in range(1,3):
            shake("l",3,1)
            shake("r",3,2)
        turnRight(4,2.57)
        rotate(4,.55)

#call to dance
dance()
    

