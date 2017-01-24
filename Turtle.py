""" Create a Turtle, name it, make it BLUE and draw a Smiley Face"""

import turtle

Turt = turtle.Turtle()

def SmileyFace():
    Turt.color('Blue')
    Turt.pu()
    Turt.forward(300)
    Turt.pd()
    Turt.left(225)
    for i in range(13):
        Turt.forward(50)
        Turt.right(7.2)
    Turt.pu()
    Turt.home()
    Turt.left(90)
    Turt.forward(250)
    Turt.left(90)
    Turt.forward(100)
    Turt.pd()
    Turt.begin_fill()
    Turt.circle(50)
    Turt.end_fill()
    Turt.right(180)
    Turt.pu()
    Turt.forward(200)
    Turt.right(90)
    Turt.forward(100)
    Turt.left(90)
    Turt.pd()
    Turt.begin_fill()
    Turt.circle(50)
    Turt.end_fill()
    Turt.pu()
    Turt.home()
    Turt.right(90)

    input()
SmileyFace()
