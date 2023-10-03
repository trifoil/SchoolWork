class Humain:
    def __init__(self,age, nom , date_anniversaire,sexe):
        self.__age = age
        self.__nom = nom
        self.__date_anniversaire = date_anniversaire
        self.__sexe = sexe
    

    def calculer_date_naissance(self,age,date_anniversaire):
        date_de_naissance = date_anniversaire + "/" + (2023 - age)
        return date_de_naissance
    

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        self.__age = value

    @property
    def nom(self):
        return self.__nom
    
    @nom.setter
    def nom(self,value):
        self.__nom=value 
    
    @property
    def date_anniversaire(self):
        return self.__date_anniversaire
    
    @date_anniversaire.setter
    def date_anniversaire(self,value):
        self.__date_anniversaire = value 

    @property
    def sexe(self):
        return self.__sexe
    
    @sexe.setter
    def sexe(self,value):
        self.__sexe = value

class Homme(Humain):
    def __init__ (self,force,nom,age,date_anniverdaire,sexe="masculin"):
        super().__init__(nom,age,date_anniverdaire,sexe)
        self.__force = force
    def mesurer_force(self,force):
        if force >= 10:
            print("g²")
    @property
    def force(self):
        return self.__force
    
    force.setter
    def force(self,value):
        self.__force=value
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        self.__age = value

    @property
    def nom(self):
        return self.__nom
    
    @nom.setter
    def nom(self,value):
        self.__nom=value 
    
    @property
    def date_anniversaire(self):
        return self.__date_anniversaire
    
    @date_anniversaire.setter
    def date_anniversaire(self,value):
        self.__date_anniversaire = value 

    @property
    def sexe(self):
        return self.__sexe
    
    @sexe.setter
    def sexe(self,value):
        self.__sexe = value

    def afficher_infos(self,nom, age, date_anniversaire,force):
        print(f"Mon nom est {nom}, j'ai {age} ans et mon anniversaire est la {date_anniversaire} et ma force est de {force}")

Lambda = Homme(force = 10, nom = "Lambda", age = 27, date_anniverdaire="25/08")
Lambda.afficher_infos(nom = input("saisissez un nom: "), age = input("saisissez l'age: "), date_anniversaire="25/08",force=10)