def eleMax(liste, debut = 0, fin = 0):
    max = liste[debut]

    if not fin:
        fin = len(liste) - 1 

    for i in range(debut, fin):
        if liste[i] > max:
            max = liste[i]

    return max


serie = [9, 3, 6, 1, 7, 5, 4, 8, 2]
print(eleMax(serie))
print(eleMax(serie, 2, 5))
