"""
Marque: attribut d'instance 
Modèle: attribut d'instance 
Nombre de voiture: attribut de classe
année : attribut d'instance
couleurs disponibles: attribut de classe
couleur: attribut d'instance
kilométrage : attibit d'instance
"""


class Voiture:
    nombre_de_voitures = 0
    couleurs_disponibles = {"noir","rouge","blue","blanc"}
    def __init__(self,marque,modele,annee,couleur,kilometrage):
        self.__marque = marque
        self.__modele = modele 
        self.__annee = annee
        self.__couleur= couleur
        self.__kilometrage = kilometrage
        Voiture.nombre_de_voitures += 1
        print(self.nombre_de_voitures)

    def changer_couleur (self, couleur):
        if couleur in self.couleurs_disponibles:
            self.__couleur= couleur
        else :
            print("mauvaise couleur")
    
    def afficher_informations(self):
        print(f"Marque: {self.__marque}")
        print(f"Modèle: {self.__modele}")
        print(f"Année: {self.__annee}")
        print(f"Couleur: {self.__couleur}")
        print(f"Killométrage: {self.__kilometrage}")
        print(f"Nombre de voitures: {Voiture.nombre_de_voitures}")
    
    