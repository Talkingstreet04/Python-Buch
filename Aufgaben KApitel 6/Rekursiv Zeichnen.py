from turtle import *


def baum(x):
    if x < 10\
            : return
    else:
        forward(x)
        left(90)
        baum(x*0.5)
        right(180)
        baum(x*0.5)
        left(90)
        back(x)

speed(1)
baum(40)
