class voiture():
    def __init__(self,vitesse,marque,demarree,portes,couleur):
        self._vitesse = vitesse
        self._marque = marque
        self._demarree = demarree
        self._portes = portes
        self._couleur = couleur 

    def afficherInfo(self):
        print(self._vitesse)
        print(self._marque)
        print(self._demarree)
        print(self._portes)
        print(self._couleur)

    def demarer(self):
        
