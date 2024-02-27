# Prise de note - prog-tp - N01

class Nom_de_classe: # le nom d'une classe commence par une majuscule.
    pass

class Etudiant:
    # Constructeur, premiere methode qui est execute lors de l'instanciation.
    def __init__(self): # ! il prend 'self' en premier parametre, comme toutes les methodes en python.
        pass

class Prof:
    attribut: str # on dit a la classe que l'attribut 'attribut' existe et est de type 'str'
    
    # ! C'est dans le constructeur la qu'on donne une valeur de base aux attributs de l'instance.
    def __init__(self, value: str): 
        self.attribut = value

class Private:
    __private_attribut: str # private (-)
    #_protected_attribut # protected (#)
    # public_attribut # public (+)

    def __init__(self, value: str):
        self.__private_attribut = value

    @property # on dit que la methode en dessous retourne une propriete (__private_attribut).
    def private_attribut(self):
        return self.__private_attribut
    
    # ! Attention il n'y a pas de setter sans getter (@proprety) !
    @private_attribut.setter # On dit que la methode en dessous est le setter de private_attribut
    def private_attribut(self, value: str):
        assert isinstance(value, str) # On envoie une erreur si le type de 'value' n'est pas un str
        self.__private_attribut = value

def main():
    nom_instance: Nom_de_classe = Nom_de_classe() # Cree une instance de Nom_de_classe dans "mon_instance"

    instance_of_private: Private = Private("Valeur...")
    print(f"Attribut: {instance_of_private.private_attribut}")
    instance_of_private.private_attribut = "Nouvelle valeur..."
    print(f"Attribut: {instance_of_private.private_attribut}")
    
    try:
        instance_of_private.private_attribut = 123
    except:
        print("Il y a eu une erreur lors de l'execution.")

if __name__ == "__main__":
    main()

# ! Ces notes ne sont pas forcement correctes (voir syntheses). !