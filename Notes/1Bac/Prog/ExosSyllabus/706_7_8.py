from turtle import *

def carre(taille, couleur, angle):
    "fonction qui dessine un carré de taille et de couleur déterminées"
    color(couleur)
    c =0
    left(angle=angle)
    down()
    while c <4:
        forward(taille)
        right(90)
        c = c +1
    up()
def triangle(taille, couleur, angle):
    color(couleur)
    c = 0
    left(angle=angle)
    down()
    while c < 3:
        forward(taille)
        right(120)
        c += 1
    up()

def etoile5(taille, couleur, angle):
    color(couleur)
    c = 0
    left(angle=angle)
    down()
    while c < 5:
        forward(taille)
        right(180-36)
        c += 1
    up()

def etoile6(taille, couleur, angle):
    initPos = pos()
    color(couleur)
    left(angle=angle)
    triangle(taille=taille, couleur=couleur, angle=0)
    forward(taille/1.5)
    seth(heading() -60)
    backward(taille/3)
    triangle(taille=taille, couleur=couleur, angle=0)

    setpos(initPos, None)
    seth(0)

etoile6(100, "blue", 0)


# Exo 706
# up()
# t = 100
# forward(-800)
# for i in range(0, 5):
#     carre(t, "blue", 0)
#     forward(t + 10)
#     triangle(t, "blue", 0)
#     forward(t + 10)
#     t += 30




mainloop()