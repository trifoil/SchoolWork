class Voiture:
    nombresDeVoitures = 0
    couleursDisponibles = ["Rouge", "Vert", "Bleu",
                          "Noire", "Grise"]

    def __init__(self, marque="", modèle="", année=0, couleur="", kilométrage=0):
        """
        Initialise une nouvelle instance de Voiture

        :param marque: Marque de la voiture
        :param modèle: Modèle de la voiture
        :param année: Année de fabrication de la voiture
        :param couleur: Couleur de la voiture
        :param kilométrage: Kilométrage de la voiture
        :raises ValueError: Si la couleur n'est pas disponible
        """
        self.__marque = marque
        self.__modèle = modèle
        self.__année = année
        self.__kilométrage = kilométrage
        if couleur.capitalize() in Voiture.couleursDisponibles:
            self.__couleur = couleur
        else:
            raise ValueError("Couleur non disponible. Les couleurs disponibles sont : {}".format(
                Voiture.couleursDisponibles))
        Voiture.nombresDeVoitures += 1

    def __del__(self):
        Voiture.nombresDeVoitures -= 1

    def changer_couleur(self, couleur: str):
        """
        Change la couleur de la voiture

        :param couleur: Nouvelle couleur de la voiture
        :raises ValueError: Si la couleur n'est pas disponible
        """
        if couleur.capitalize() in Voiture.couleursDisponibles:
            self.__couleur = couleur
        else:
            raise ValueError("Couleur non disponible. Les couleurs disponibles sont : {}".format(
                Voiture.couleursDisponibles))

    def afficher_informations(self):
        """Affiche les informations de la voiture"""
        print("\nMarque :", self.__marque)
        print("Modèle :", self.__modèle)
        print("Année :", self.__année)
        print("Couleur", self.__couleur)
        print("Kilométrages", self.__kilométrage)
        print("Nombre total de voitures :", Voiture.nombresDeVoitures, "\n")


if __name__ == "__main__":
    voiture1 = Voiture("Ford", "Model A", 1903, "Noire", 350000)
    voiture1.afficher_informations()
    voiture2 = Voiture("Ford", "Model B", 1904, "Noire", 340000)
    voiture2.afficher_informations()
    print(voiture1.__dict__)
    print(voiture2.__dict__)
    del voiture2
    print(Voiture.changer_couleur.__doc__)