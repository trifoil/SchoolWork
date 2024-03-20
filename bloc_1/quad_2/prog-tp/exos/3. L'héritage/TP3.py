class Personnage:
    def __init__(self, nom, puissance, pointsDeVie):
        self.__nom = nom
        self.__puissance = puissance
        self.__points_de_vie = pointsDeVie
    
    def attaquer(self, other):
        other.perdre_point_de_vie(self.puissance)
    
    def perdre_point_de_vie(self, degats):
        self.__points_de_vie -= degats
    
    def est_ko(self):
        return self.__points_de_vie <= 0

class SuperHero(Personnage):
    def __init__(self, nom, puissance, pointsDeVie, nom_secret, est_vivant=True):
        super().__init__(nom, puissance, pointsDeVie)
        self.__nom_secret = nom_secret
        self.__est_vivant = est_vivant
    
    def attaquer(self, other):
        if isinstance(other, SuperVilain):
            other.perdre_point_de_vie(self.puissance * 2)
        else:
            other.perdre_point_de_vie(self.puissance)
    
    def utiliser_pouvoir_special(self, augmentation_puissance=10):
        self.puissance += augmentation_puissance

class SuperVilain(Personnage):
    def __init__(self, nom, puissance, pointsDeVie, nom_code="", heros_combattus=[], but=""):
        super().__init__(nom, puissance, pointsDeVie)
        self.__nom_code = nom_code
        self.__heros_combattus = heros_combattus
        self.__but = but
