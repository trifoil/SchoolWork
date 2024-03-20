from TP1 import Humain

class Sortilege:
    def __init__(self, formule, effet, impardonnable=False):
        self.__formule = formule
        self.__effet = effet
        self.__impardonnable = impardonnable

    def SeLancer(self):
        print(f"Le sort '{self.formule}' a été lancé avec succès.")

    def Description(self):
        print(f"Formule : {self.formule}\nEffet : {self.effet}")

    @property
    def formule(self):
        return self.__formule


class Sorcier(Humain):
    def __init__(self, nom="", prenom="", annéeNaissance=0, baguette="", maison=""):
        super().__init__(nom, prenom, annéeNaissance)
        self.__baguette = baguette
        self.__maison = maison
        self.__sortilegesConnus = []

    def LancerSort(self, sortilege: Sortilege):
        if sortilege in self.__sortilegesConnus:
            print("Lancement du sort :", sortilege.formule)
            sortilege.SeLancer()
        else:
            raise ValueError("Le sort n'est pas connu")

    def AjouterSort(self, sortilege: Sortilege):
        self.__sortilegesConnus.append(sortilege)


if __name__ == "__main__":
    sortilege1 = Sortilege("Expelliarmus", "Désarme l'adversaire")
    sorcier1 = Sorcier("Harry", "Potter", 1980, "Épicéa, plume de phénix", "Gryffondor")

    sorcier1.AjouterSort(sortilege1)
    sorcier1.LancerSort(sortilege1)
