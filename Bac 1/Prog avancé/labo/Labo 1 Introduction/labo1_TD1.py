class serpent():
    def __init__ (self,longueur, couleur, vitesse, venimeux):
        self._longueur = longueur
        self._couleur = couleur
        self._vitesse = vitesse
        self._venimeux = venimeux

    def afficherInfo(self):
        print(self._longueur)
        print(self._couleur)
        print(self._vitesse)
        print(self._venimeux)

    def seDeplacer(self,direction ):
        self._direction = direction 
        print(self._direction)
    
    def manger(self,manger):
        self._manger = manger
        print(self._manger)
