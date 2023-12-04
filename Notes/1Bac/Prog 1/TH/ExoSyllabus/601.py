milesParHeure = float(input("miles/h : "))
metreParHeure = milesParHeure * 1609

kilometreParHeure = metreParHeure / 1000
metreParSeconde = kilometreParHeure / 3.6


print("%.4f km/h" % kilometreParHeure)
print("%.4f m/s" % metreParSeconde)
