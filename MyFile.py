import turtle
Poly = turtle.Turtle()
n = int(input('Enter a number:'))
def polygon(n):
    for i in range(n):
        Poly.forward(50)
        Poly.left(360/n)
    input()
polygon(n)
