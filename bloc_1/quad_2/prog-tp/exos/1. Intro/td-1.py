# Exo:
# Créer une classe « Serpent » qui possède les caractéristiques suivantes :
#   - Longueur
#   - Couleur
#   - Vitesse
#   - Venimeux
#
# Elle possèdera également les méthodes suivantes :
#   - ‘afficherInfo()’, pour afficher les différentes infos de l’objet
#   - ‘seDeplacer()’, pour permettre à l’objet de se déplacer dans une direction
#   - ‘manger()’, pour définir que le serpent a mangé.

class Serpent:
    longueur: float
    couleur: str
    vitesse: float
    estVenimeux: bool

    def __init__(self, longeur: float, couleur: str, vitesse: float, estVenimeux: bool):
        self.longueur = longeur
        self.couleur = couleur
        self.vitesse = vitesse
        self.estVenimeux = estVenimeux

    def afficherInfo(self):
        estVenimeuxString = "Oui" if self.estVenimeux else "Non"
        print(
            f"Information sur le serpent:\n",
            f"- Longueur: {self.longueur}\n",
            f"- Couleur: {self.couleur}\n",
            f"- Vitesse: {self.vitesse}\n",
            f"- Venimeux: {estVenimeuxString}\n"
        )

    def seDeplacer(self, direction):
        print(f'Le serpent se déplace dans la direction "{direction}" à une vitesse de {self.vitesse} km/h')
    
    def manger(self, repas):
        self.longueur += 1
        print(f'Le serpent a mangé "{repas}", il gagne +1 cm en longueur, ce qui lui fait {self.longueur} cm au total.')

def main():
    mon_serpent: Serpent = Serpent(256, "Rouge", 3, True)
    print(f"{type(mon_serpent)}\n")

    mon_serpent.afficherInfo()
    mon_serpent.seDeplacer("Nord")
    mon_serpent.manger("souris")

if __name__ == "__main__":
    main()