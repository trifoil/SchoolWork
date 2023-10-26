from turtle import *

def triangle(couleur, x=0, y=0):
    up()
    setposition(x, y)
    down()
    color(couleur)
    forward(100)
    left(120)
    forward(100)
    left(120)
    forward(100)
    left(120)
    up()

triangle("blue")
triangle("blue", 200)


mainloop()