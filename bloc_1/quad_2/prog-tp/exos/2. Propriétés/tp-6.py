class Joueur:
    nombre_joueurs = 0
    def __init__(self, nom:str, age:int, score:int, niveau:int):
        self._nom = nom
        self._age = age
        self._score = score
        self._niveau = niveau
        Joueur.nombre_joueurs += 1
    
    def __del__(self):
        Joueur.nombre_joueurs -= 1

    def afficher_informations(self):
        print("\nNom", self._nom)
        print("Age", self._age)
        print("Score", self._score)
        print("Niveau", self._niveau)

    def augmenter_score(self, n):
        self._score += n
    
class JoueurExpert(Joueur):
    def __init__(self, nom: str, age: int, score: int, niveau: int, bonus:int):
        super().__init__(nom, age, score, niveau)
        self._bonus = bonus
    
    def afficher_informations(self):
        super().afficher_informations()
        print("Bonus", self._bonus)

    def afficher_bonus(self):
        print("Bonus", self._bonus)


if __name__ == "__main__":
    joueur = Joueur("John", 30, 20, 7)
    joueurExpert = JoueurExpert("Jane", 40, 50, 17, 2)
    
    print(joueur.__dict__)
    joueur.augmenter_score(5)
    joueur.afficher_informations()
    
    print(joueurExpert.__dict__)
    joueurExpert.augmenter_score(5)
    joueurExpert.afficher_informations()