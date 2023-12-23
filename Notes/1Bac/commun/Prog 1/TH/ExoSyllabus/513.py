nbrList = [32, 5, 12, 8, 3, 75, 2, 15]
maxNbr = nbrList[0]
for i in range(0, len(nbrList)):
    if nbrList[i] > maxNbr:
        maxNbr = nbrList[i]

print("le plus grand élément de cette liste a la valeur", maxNbr)
