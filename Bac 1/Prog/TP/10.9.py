#page 121 ex 10.9

x = input("entrez n'importe quoi: ")
def estUnChiffre(x):
    j=0
    y = "0123456789"
    for j in x:
        if j in y:
            print(str(j) + ": oui")
            
        else: 
            print(str(j) + ": non")
            
            
    
estUnChiffre(x)
