import datetime

class humain():
    def __init__(self,nom,prenom,annee_de_naissance,enfants = None):
        self._nom = nom
        self._prenom = prenom
        self._annee_de_naissance = annee_de_naissance
        if enfants == None: 
            enfants = []
        self._enfants = enfants
    
    def calculer_age(self):
        moment_actuel = datetime.datetime.now()   
        date = moment_actuel.date()
        age = date.year - self._annee_de_naissance
        self._age = age
        print(age)

    def sePresenter(self):

        print(f"Nom: {self._nom}\nPrenom: {self._prenom}\nAge: {self._age}")
    
    @property
    def nom(self):
        return self._nom
    
    @nom.setter
    def nom(self, value):
        self._nom = value


    #def reconnaissanceparentale(self): 


#toto = humain("J", "D", 1920)

#toto.nom = "Ben"

#print(toto.nom)