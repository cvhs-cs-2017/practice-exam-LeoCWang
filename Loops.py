"""Use a loop to make a turtle draw a shape that is has at least 100 sides and
that shows symmetry.  The entire shape must fit inside the screen"""
import turtle
sven = turtle.Turtle()
def hectagon():
    sven.speed(0)
    for i in range(100):
        sven.fd(10)
        sven.left(3.6)
    input()
hectagon()
