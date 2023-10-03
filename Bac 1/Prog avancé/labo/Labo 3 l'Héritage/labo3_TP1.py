import datetime

class Humain():
    def __init__(self,nom,prenom,annee_de_naissance,enfants = None):
        self._nom = nom
        self._prenom = prenom
        self._annee_de_naissance = annee_de_naissance
        if enfants is None: 
            enfants = []
        self._enfants = enfants
    
    def calculer_age(self):
        moment_actuel = datetime.datetime.now()   
        date = moment_actuel.date()
        age = date.year - self._annee_de_naissance
        return age

    def sePresenter(self):

        print(f"Nom: {self._nom}\nPrenom: {self._prenom}\nAge: {self.calculer_age()}")
    
    @property
    def nom(self):
        return self._nom
    
    @nom.setter
    def nom(self, value):
        self._nom = value

class Moldu(Humain):
    def __init__(self,nom,prenom,annee_de_naissance,travail,connaissance_de_la_magie = False):
        super().__init__(nom,prenom,annee_de_naissance)
        self._travail = travail
        self._connaissance_de_la_magie = connaissance_de_la_magie
    
    def sePresenter(self):
        super().sePresenter() 
        print(f"Travail: {self._travail}\nConnaissance de la magie: {self._connaissance_de_la_magie} Age:{self.calculer_age()}")

    def découvrir_la_magie(self):
        self._connaissance_de_la_magie = True
    
class Sorcier(Humain):
    maison_disp =["Gryffondor", "Poufsouffle", "Serdaigle", "Serpentard"]
    def __init__(self, nom, prenom, annee_de_naissance,baguette,maison,sortilèges_connus = None,enfants=None):
        super().__init__(nom, prenom, annee_de_naissance, enfants)

        
        self._baguette = baguette
        self._maison = maison    
        if sortilèges_connus is None:
            sortilèges_connus = []
        self._sortileges_connus = sortilèges_connus

    def lancersort(self,sorts):

        if sorts in self._sortileges_connus:
            print("Sort lancé")
        else:
            print("sort inconnu")
    
    def apprendresort(self,nouveau_sort):
        if nouveau_sort in self._sortileges_connus:
            print("sort déja connu")
        else: 
            self._sortileges_connus.append (nouveau_sort)
    def SePresenter(self):
        super().sePresenter()
        print(f"Baquette:{self._baguette}\nmaison:{self._maison}\nAge:{self.calculer_age()}\n")




    


        
