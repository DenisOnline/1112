from turtle import *


def draw_wheel(color_spoke, len_spoke, size_spoke, color_tire, size_tire):
    shape("turtle")
    pensize(size_spoke)
    color(color_spoke)
    for i in range(10):
        forward(len_spoke)
        left(180)
        forward(len_spoke)
        left(180 - 36)
    penup()
    right(90)
    forward(len_spoke)
    left(90)
    color(color_tire)
    pendown()
    pensize(size_tire)
    circle(len_spoke)


print(draw_wheel("blue", 180, 3, "black", 12))

a = 6
b = 2
for i in range(1, 10):
    a += i
    b *= i
    print("a = ", a)
    print("b = ", b)