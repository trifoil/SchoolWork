def changeCar(ch1, ca1, ca2, debut=0, fin=0):
    lst = [*ch1]
        
    if not fin:
        fin = len(ch1)

    for i in range(debut, fin):
        if lst[i] == ca1:
            print(lst[i])
            lst[i] = ca2

    return ''.join(lst)


phrase = 'Ceci est une phrase.'
print(changeCar(phrase, ' ', '*'))
