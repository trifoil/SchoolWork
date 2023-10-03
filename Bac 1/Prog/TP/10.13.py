x = input("entrer un phrase")

def comptemaj(x):
    majuscules = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    k = 0
    for j in range(len(x)):
        if x[j] in majuscules:
            k+=1
    print (k)
    
comptemaj(x)
