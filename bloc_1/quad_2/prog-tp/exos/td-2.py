# Exo
# Créer une classe « Voiture » qui possède les caractéristiques suivantes :
#   - Couleur
#   - Vitesse
#   - Portes
#   - Marque
#   - Demarree ?
#
# Elle possèdera également les méthodes suivantes :
#   - ‘afficherInfo()’, pour afficher les différentes infos de l’objet
#   - ‘avancer()’, pour permettre à l’objet de se déplacer dans une direction
#   - ‘demarrer()’, pour permettre à la voiture de se mettre en route.

class Voiture():
    couleur: str
    vitesse: float
    portes: int
    marque: str
    estDemaree: bool

    def __init__(self, couleur: str, vitesse: float, portes: int, marque: str):
        self.couleur = couleur
        self.vitesse = vitesse
        self.portes = portes
        self.marque = marque
        self.estDemaree = False

    def afficherInfo(self):
        estDemareeString = "Oui" if self.estDemaree else "Non"
        print(
            f"Information sur la voiture:\n",
            f"- Marque: {self.marque}\n",
            f"- Couleur: {self.couleur}\n",
            f"- Vitesse: {self.vitesse}\n",
            f"- Portes: {self.portes}\n",
            f"- Venimeux: {estDemareeString}\n"

        )
        
    def avancer(self, direction):
        if (self.estDemaree):
            print(
                f"La voiture avance vers '{direction}' à la vitesse de {self.vitesse} km/h\n"
                )
        else:
            print(
                f"Vous appuyez frénétiquement sur l'accélérateur mais rien ne se passe.",
                f"Peut-être devriez-vous démarrer le moteur avant ?\n"

                )
    
    def demaree(self):
        self.estDemaree = True
        print("Vous mettez les clés dans le contact et tournez la clé. Bien que vous ne sachiez pas comment l'éteindre, une grande joie vous envahit.\n")

    
def main():
    ma_voiture: Voiture = Voiture("Rouge", 160, 4, "BMW")
    print(f"{type(ma_voiture)}\n")

    ma_voiture.afficherInfo()

    ma_voiture.avancer("Sud")

    ma_voiture.demaree()

    ma_voiture.avancer("Sud")

if __name__ == "__main__":
    main()