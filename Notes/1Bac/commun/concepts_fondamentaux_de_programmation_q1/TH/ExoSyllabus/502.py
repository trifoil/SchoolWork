from math import *

angle = float(input("Entrez un angle en radians : "))

#Formule pour passer de rad à deg
degre = angle*(180/pi)

# modf du module math prend seulement la partie fractionnaire
# Si j'ai 1.5 rad, 0.5 * 60 = 30 minutes
minute = modf(degre)[0] * 60
seconde = modf(minute)[0] * 60

print(f"{angle} en degrés : {int(degre)}° {int(minute)}\' {int(seconde)}\"")