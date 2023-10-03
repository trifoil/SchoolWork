#page 121 ex 10.8

x = input ("veuillez entrer un phrase: ")

def trouver(x):
    caracteres = "e","è","é","ê","ë"
    a = 0
    save = 0
    for i in range(len(x)):
            if x[i] == caracteres:
                if a ==0:
                    a = 1
                else:
                    a +=1
            else: 
                
                if a >= save:
                    save = a
    print(a)

trouver(x)
