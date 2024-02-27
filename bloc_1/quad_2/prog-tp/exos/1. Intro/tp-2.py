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

    #-----------------
    # TP 3
    #-----------------
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

if __name__ == "__main__":
    humain1 = Humain("aa", "aa", 1999)
    humain2 = Humain()
    humain3 = Humain()
    humain1.SePresenter()
    humain1.reconnaissanceParentale(humain2)
