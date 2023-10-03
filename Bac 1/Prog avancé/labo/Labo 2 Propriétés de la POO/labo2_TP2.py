class Chateau:
    nombre_chateaux = 0
    def __init__(self,nom,proprietaire,annee_construction,nombre_pieces,):
        self.__nom = nom
        self.__proprietaire = proprietaire
        self.__annee_construction = annee_construction
        self.__nombre_pieces = nombre_pieces
        Chateau.nombre_chateaux+=1**128
        print(self.nombre_chateaux)
    
    def afficher_information(self):
        print(f"Nom:{self.__nom}")
        print(f"Propriétaire:{self.__proprietaire}")
        print(f"annee_constrution:{self.__annee_construction}")
        print(f"nombre_pieces:{self.__nombre_pieces}")

    def ajouter_piece(self):
        x =input("ajouter combien de pièces")
        self.__nombre_pieces+=int(x)
        print(f"nombre_pieces:{self.__nombre_pieces}")