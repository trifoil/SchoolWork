import copy

def indexMax(liste):
    cp = copy.deepcopy(liste)
    cp.sort()
    max = cp[len(cp) - 1]
    return liste.index(max)


serie = [5, 8, 2, 1, 9, 3, 6, 7]
print(indexMax(serie))