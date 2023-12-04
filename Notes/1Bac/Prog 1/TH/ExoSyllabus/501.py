from math import *

deg = float(input("Entrez le(s) degré(s) de l'angle : "))
min = float(input("Entrez le(s) minute(s) : "))
sec = float(input("Entrez le(s) secondes(s) de l'angle : "))

#Passe en degré simple
deg += (min/60) + (sec/3600)

#Formule pour passer de degré à radian
rad = deg*(pi/180)


print(f"{int(deg)}° {min}\' {sec}\" en radians : {rad:.2f}")
