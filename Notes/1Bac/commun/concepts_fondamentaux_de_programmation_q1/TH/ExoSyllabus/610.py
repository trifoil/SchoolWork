nom = input("Quel est votre nom ? : ")
sexe = input("Quel est votre sexe (M ou F) ? : ")

if sexe.lower() == "m":
    print("Cher Monsieur", nom)
elif sexe.lower() == "f":
    print("Chère Mademoiselle", nom)