from math import *
a = int(input("a : "))
b = int(input("b : "))
c = int(input("c : "))
perimetre = a + b + c
dP = perimetre/2
aire = sqrt(dP*(dP-a)*(dP-b)*(dP-c))

print("%.3f" % aire)