from random import randrange

class Vaisseau:
    def __init__(self, nom, modele, longueur, largeur, vitesse, integrite):
        self.nom = nom
        self.modele = modele
        self.longueur = longueur
        self.largeur = largeur
        self.vitesse = vitesse
        self.integrite = integrite
    
    def __str__(self, nom, modele, longueur, largeur, vitesse):
        return "{} : {} {} {} {} {}".format(nom, modele, longueur, largeur, vitesse)

    def accelerer(self, vitesse_supplementaire):
        self.vitesse = vitesse_supplementaire

class Arme():
    def __init__(self, nom:str, degats: int):
        self.nom = nom
        self.degats = degats

class Chasseur(Vaisseau):
    def __init__(self, nom, modele, longueur, largeur, vitesse, integrite):
        super().__init__(nom, modele, longueur, largeur, vitesse, integrite)
        self.armes = []
        self.furtif = True
    
    def afficher_armes(self):
        for i in self.armes:
            print(i)
    
    def activer_furtivite(self):
        self.furtif != self.furtif

    def attaquer(self, vaisseau, arme: Arme):
        vaisseau.integrite -= self.armes[arme].degats

class VaisseauDeCombat(Vaisseau):
    def __init__(self, nom, modele, longueur, largeur, vitesse, integrite, armure:int):
        super().__init__(nom, modele, longueur, largeur, vitesse, integrite)
        self.armure = armure
        self.bouclierActif = False
        
    def afficher_armure(self):
        print(self.armure)

    def activer_bouclier(self, armure:int):
        self.armure = armure
        self.bouclierActif = True

class FlotteSpatiale:
    def __init__(self, nom, vaisseaux:list):
        self.nom = nom
        self.vaisseaux = []

    def ajouter_vaisseau(self, vaisseau):
        self.vaisseaux.append(vaisseau)

    def supprimer_vaisseau(self, vaisseau):
        self.vaisseaux.remove(vaisseau)

    def afficher_vaisseaux(self):
        for i in self.vaisseaux:
            print(i)

    def attaquer_flotte(self, flotte_ennemie):
        fe = flotte_ennemie.vaisseaux
        
        cnt = 0
        for i in fe:
            vaisseauAttaqué = fe[randrange(0, len(fe) - 1)]
            vaisseauAttanquant = self.vaisseaux[cnt]
            cnt += 1

            








        
        
        


        


