class Chateau:

    nombre_chateaux = 0

    def __init__(self, nom="", proprietaire="", année_construction=0, nombres_pièces=0):
        self.__nom = nom
        self.__proprietaire = proprietaire
        self.__année_construction = année_construction
        self.__nombres_pièces = nombres_pièces
        Chateau.nombre_chateaux += 1

    def __del__(self):
        Chateau.nombre_chateaux -= 1

    def afficher_informations(self):
        print("\nNom :", self.__nom)
        print("Propriétaire :", self.__proprietaire)
        print("Année de construction :", self.__année_construction)
        print("Nombre de pièces :", self.__nombres_pièces, "\n")

    def ajouter_pièces(self, nombre: int):
        """Ajouter des pièces
        
        Params:
            nombre (int) : Nombre de pièces à ajouter

        Raises:
            ValueError: Si le nombre n'est pas un entier >= 0
        """
        if nombre >= 0 and type(nombre) == int:
            self.__nombres_pièces += nombre
        else:
            raise ValueError("Nombre de pièces négatifs ou non entier.")


if __name__ == "__main__":
    chateau1 = Chateau("Versaille", "Louis XIV", 1631, 246)
    print(chateau1.__dict__)
    chateau1.afficher_informations()
    chateau2 = Chateau("Chambord", "François I", 1519, 213)
    print(chateau2.__dict__)
    chateau2.ajouter_pièces(2)
    chateau2.afficher_informations()
