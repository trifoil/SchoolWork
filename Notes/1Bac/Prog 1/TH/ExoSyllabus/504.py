capitalDepart = capital = float(input("Capital de départ : "))
for i in range(1, 21):
    capital *= 1.043

print("Valeur totale après 20 ans : %.2f" % capital)
print("Total des intérêts gagnés : %.2f" % (capital - capitalDepart))