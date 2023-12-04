# Page 
def read_int(prompt, min, max): 
    while True:
        try:
            v = int(input(prompt))
            if not min <= v <= max:
                raise Exception()
        except ValueError:
            print("Erreur: saisie incorrecte")
        except:
            print("Erreur : la valeur n'est pas dans la plage autorisée (min.. max)")
        else:
            return v
 
 
v = read_int("Entrer un nombre entre -10 et 10: ", -10, 10)
print("Le nombre est:", v)