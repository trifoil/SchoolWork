class Joueur:
    def __init__(self, nom: str, age: int, taille: int, poste: str):
        self.nom = nom
        self.age = age
        self.taille = taille
        self.poste = poste

    def __str__(self):
        return f"Nom: {self.nom}, Age: {self.age}, Taille: {self.taille}, Poste: {self.poste}"

class Equipe:
    def __init__(self, nom: str):
        self.nom = nom
        self.joueurs = []

    def add_joueur(self, joueur: Joueur):
        self.joueurs.append(joueur)

    def remove_joueur(self, joueur: Joueur):
        self.joueurs.remove(joueur)

    def moyenne_age(self):
        if self.joueurs:
            return sum(joueur.age for joueur in self.joueurs) / len(self.joueurs)
        else:
            return 0

    def joueur_plus_grand(self):
        if self.joueurs:
            return max(self.joueurs, key=lambda joueur: joueur.taille)
        else:
            return None

    def joueur_plus_petit(self):
        if self.joueurs:
            return min(self.joueurs, key=lambda joueur: joueur.taille)
        else:
            return None

    def joueur_au_poste(self, poste: str):
        for joueur in self.joueurs:
            if joueur.poste == poste:
                return joueur
        return None

equipe_profs = Equipe("Equipe des Profs")
equipe_groupe = Equipe("Votre Groupe")

joueur1 = Joueur("Professeur A", 40, 180, "Entraîneur")
joueur2 = Joueur("Professeur B", 45, 175, "Défenseur")
joueur3 = Joueur("Étudiant A", 20, 175, "Attaquant")
joueur4 = Joueur("Étudiant B", 22, 185, "Milieu de terrain")

equipe_profs.add_joueur(joueur1)
equipe_profs.add_joueur(joueur2)
equipe_groupe.add_joueur(joueur3)
equipe_groupe.add_joueur(joueur4)

print(equipe_groupe.moyenne_age())
print(equipe_profs.moyenne_age())
print(equipe_groupe.joueur_plus_grand())
print(equipe_profs.joueur_plus_grand())
