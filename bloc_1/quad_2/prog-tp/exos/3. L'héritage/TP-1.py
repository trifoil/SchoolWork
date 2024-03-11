class Humain():
    def __init__(self, nom="", prenom="", annéeNaissance=0):
        self.__nom = nom
        self.__prenom = prenom
        self.__annéeDeNaissance = annéeNaissance
        self.__enfants = []

    def __CalculerAge(self):
        return 2024 - self.__annéeDeNaissance

    def SePresenter(self):
        print(self.__prenom, self.__nom, self.age)

    def reconnaissanceParentale(self, humain):
        if type(humain) != Humain:
            return None
        else:
            self.__enfants.append(humain)

    @property
    def nom(self):
        return self.__nom

    @property
    def prenom(self):
        return self.__prenom

    @property
    def age(self):
        return self.__CalculerAge()

    @property
    def enfants(self):
        return self.__enfants


class Moldu(Humain):
    def __init__(self, nom="", prenom="", anneeNaissance=0, travail="Ne connait pas la magie"):
        Humain.__init__(self, nom, prenom, anneeNaissance)
        self.__travail = travail
    
    def SePresenter(self):
        super().SePresenter()
        print("Travail :", self.__travail)
    
    def DécouvrirMagie():
        pass

class Sorcier(Humain):
    def __init__(self, nom="", prenom="", annéeNaissance=0, baguette="", maison=""):
        super().__init__(nom, prenom, annéeNaissance)
        self.__baguette = baguette
        self.__maison = maison
        self.__sortilegesConnus = []

    def lancerSort(self, sortilege):
        if sortilege in self.__sortilegesConnus:
            print("Lancement du sort :", sortilege)
        else:
            raise ValueError("Le sort n'est pas connu")
    def ApprendreSort(self, sortilege):
        self.__sortilegesConnus.append(sortilege)
    
    def SePresenter(self):
        super().SePresenter()
        print("Maison :", self.__maison)
    

if __name__ == "__main__":
    humain1 = Humain("aa", "aa", 1999)
    humain2 = Humain()
    humain3 = Humain()
    humain1.SePresenter()
    humain1.reconnaissanceParentale(humain2)

