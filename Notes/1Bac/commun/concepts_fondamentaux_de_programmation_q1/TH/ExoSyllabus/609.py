annee = int(input("année : "))
bi = False


if(annee % 4 == 0):
    bi = True
    if(annee % 100 == 0):
        bi = False
        if(annee % 400 == 0):
            bi = True
    

print(bi)