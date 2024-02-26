# Exo
# Créer une classe « Monstre » qui possède les caractéristiques suivantes :
#   - Race (Dragon, Gobelin, Fantomes, etc)
#   - Type (Humanoïdes, Mort-Vivants, Aquatiques, etc)
#   - Nom
#   - Age
#   - Dangereux ?
# Elle possèdera également les méthodes suivantes :
#   - ‘afficherInfo()’, pour afficher les différentes infos de l’objet
#   - ‘vieillir()’, pour permettre au monstre de vieillir
#   - ‘devenirDangereux(), pour permettre au monstre de devenir dangereux

class Monstre:
    race: str
    race_type: str
    nom: str
    age: int
    estDangereux: bool

    def __init__(self, race: str, race_type: str, nom: str, age: int, estDangereux: bool):
        self.race = race
        self.race_type = race_type
        self.nom = nom
        self.age = age
        self.estDangereux = estDangereux

    def afficherInfo(self):
        estDangereuxString = "ATTENTION, il est extrêmement dangereux." if self.estDangereux else "Il est totalement inoffensif."
        print(
            f"{self.nom} est un méchant monstre de la race {self.race} qui est de type {self.race_type}.",
            f"\nCe monstre est âgé de {self.age} ans.",
            f"\n{estDangereuxString}\n"
        )
    
    def viellir(self, age: int=1):
        self.age += age
        print(f"Le monstre a pris de l'age, il a desormais {self.age}ans\n")

    def devenirDangereux(self):
        self.estDangereux = True
        print(f"{self.nom}, le monstre inoffensif est désormais devenu un méchant monstre extrêmement dangereux, faites attention à vous !\n")

def main():
    mon_monstre = Monstre("Démon rouge", "Humanoides", "YunYun", 14, False)
    print(f"{type(mon_monstre)}\n")

    mon_monstre.afficherInfo()
    mon_monstre.viellir()
    mon_monstre.devenirDangereux()
    mon_monstre.afficherInfo()

if __name__ == "__main__":
    main()