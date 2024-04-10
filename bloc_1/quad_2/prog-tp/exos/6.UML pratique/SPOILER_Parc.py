import datetime  # Import de la bibliothèque datetime


def print_with_sep(message):
    """
    Fonction pour afficher un message avec des séparateurs
    :param message: message à afficher
    :return: "\n---------------------------" \n {message}
    """
    print("\n---------------------------")
    print(message)


class Parc:
    """
    Classe Parc
    """
    id = 0

    def __init__(self, name):  # Ajout d'une liste au départ
        """
        Constructeur de la classe Parc (1 paramètre)
        :param name: nom du parc
        """
        self._id = Parc.id
        self._name = name
        self._billets_vendus = 0
        self._argent = 0
        self._attractions = []
        Parc.id += 1

    def ajouter_attraction(self, attraction):
        """
        Méthode pour ajouter une attraction à la liste
        :param attraction: attraction à ajouter
        :return: print
        """
        if isinstance(attraction, Attraction):
            self._attractions.append(attraction)
            print_with_sep(f"{attraction} ajoutée avec succès")
        else:
            print_with_sep(f"Erreur: l'{attraction} n'est pas une attraction")

    def retirer_attraction(self, attraction):
        """
        Méthode pour retirer une attraction de la liste
        :param attraction: attraction à retirer
        :return: Print
        """
        if isinstance(attraction, Attraction):
            if attraction in self._attractions:
                self._attractions.remove(attraction)
                print_with_sep(f"{attraction} retirée avec succès")
            else:
                print_with_sep("Erreur: l'attraction n'est pas dans la liste")
        else:
            print_with_sep("Erreur: l'objet n'est pas une attraction")

    def desactiver_attraction(self, attraction):
        """
        Méthode pour désactiver une attraction
        :param attraction: attraction à désactiver
        :return: Print
        """
        if isinstance(attraction, Attraction):
            if attraction in self._attractions:
                attraction._active = False
                print_with_sep(f"{attraction} désactivée avec succès")
        else:
            print_with_sep("Erreur: l'objet n'est pas une attraction")

    def vendre_entree(self, attraction):
        """
        Méthode pour vendre une entrée à une attraction
        :param attraction: Billet pour attraction à vendre
        :return: Print
        """
        if isinstance(attraction, Attraction):
            if attraction.get_active():
                self._billets_vendus += 1
                tarif = attraction.get_billet().get_tarif()
                self._argent += tarif
                print_with_sep(f"Entrée vendue pour {attraction} à {tarif}€")
            else:
                print_with_sep("Erreur: l'attraction n'est pas active")
        else:
            print_with_sep("Erreur: l'objet n'est pas une attraction")

    def __str__(self):
        """
        Méthode pour afficher les informations du parc
        :return: Nom du parc, nombre de billets vendus, Solde, id
        """
        return (f"Nom du parc: {self._name},"
                f"Nombre de billets vendus: {self._billets_vendus},"
                f"Solde: {self._argent}€,"
                f"id: {self._id}")

    def get_attractions(self):
        """
        Méthode pour retourner la liste des attractions
        :return: _attractions
        """
        return self._attractions


class Attraction:
    """
    Classe Attraction
    """
    def __init__(self, nom, file, billet, places):
        """
        Constructeur de la classe Attraction (4 paramètres)
        :param nom: nom de l'attraction
        :param file: nombre de personnes dans la file d'attente
        :param billet: instance de la classe Billet
        :param places: places disponibles dans l'attraction
        """
        self._nom = nom
        self._file = file
        if isinstance(billet, Billet):
            self._billet = billet
        # else
        self._places = places
        self._active = True
        self._tourne = False
        print_with_sep(f"{nom} crée avec succès")

    def __str__(self):
        """
        Méthode pour afficher le nom de l'attraction
        :return: _nom
        """
        return self._nom

    def afficher_statut(self):
        """
        Méthode pour afficher les informations de l'attraction
        :return: Print
        """
        print_with_sep(f"Attraction {self._nom} :")
        print(f"File d'attente : {self._file}")
        print(f"Nombre de places disponibles : {self._places}")
        print(f"Prix d'un billet : {self._billet}")
        print(f"Attraction active : {self._active}")

    def reduire_file(self, nombre=1):
        """
        Méthode pour réduire la file d'attente
        :param nombre: int
        :return: Print
        """
        if nombre <= self._file:
            self._file -= nombre
            print_with_sep(f"Réduction de la file d'attente de '{self._nom}' de {nombre} personne.s")
        else:
            print_with_sep("Erreur: le nombre est supérieur à la file d'attente")

    def demarrer(self):
        """
        Méthode pour démarrer l'attraction
        :return: Print
        """
        # if active
        if not self._tourne:
            print_with_sep(f"L'attraction {self._nom} démarre")
            self._tourne = True
        else:
            print_with_sep(f"L'attraction {self._nom} est déjà en marche")

    def arreter(self):
        """
        Méthode pour arrêter l'attraction
        :return: Print
        """
        if self._tourne:
            print_with_sep(f"L'attraction {self._nom} s'arrête")
            self._tourne = False
        else:
            print_with_sep(f"L'attraction {self._nom} est déjà arrêtée")

    def arret_urgence(self):
        """
        Méthode pour arrêter l'attraction en cas d'urgence
        :return: Print
        """
        self._tourne = False
        print_with_sep(f"Arrêt d'urgence de l'attraction {self._nom}")

    def verifier_places(self):
        """
        Méthode pour vérifier le nombre de places disponibles
        :return: Print
        """
        if self._places > 0:
            print_with_sep(f"Il reste {self._places} places disponibles")
        else:
            print_with_sep("Il n'y a plus de places disponibles")

    def get_billet(self):
        """
        Méthode pour retourner le billet
        :return: _billet
        """
        return self._billet

    def get_file(self):
        """
        Méthode pour retourner la file
        :return: _file
        """
        return self._file

    def get_active(self):
        """
        Méthode pour retourner l'état de l'attraction
        :return: _active
        """
        return self._active

    def set_active(self, active):
        """
        Méthode pour modifier l'état de l'attraction
        :param active: bool
        :return: Print
        """
        if active or not active:
            self._active = active
            print_with_sep(f"L'attraction {self._nom} est maintenant {'active' if active else 'inactive'}")
        else:
            print_with_sep("Erreur: la valeur n'est pas un booléen")

    def get_tourne(self):
        """
        Méthode pour retourner l'état de l'attraction
        :return: _tourne
        """
        return self._tourne

    def set_tourne(self, tourne):
        """
        Méthode pour modifier l'état de l'attraction
        :param tourne: bool
        :return: Print
        """
        if tourne or not tourne:
            self._active = tourne
            print_with_sep(f"L'attraction {self._nom} est maintenant {'en marche' if tourne else 'arrêtée'}")
        else:
            print_with_sep("Erreur: la valeur n'est pas un booléen")


class Manege(Attraction):
    """
    Classe Manège
    """
    def __init__(self, nom, file, billet, places, cabines):
        """
        constructeur de la classe Manège (5 paramètres)
        :param nom: nom de l'attraction
        :param file: nombre de personnes dans la file d'attente
        :param billet: instance de la classe Billet
        :param places: places disponibles dans l'attraction
        :param cabines: nombre de cabines
        """
        super().__init__(nom, file, billet, places)
        self._cabines = cabines

    def __str__(self):
        """
        Méthode pour afficher le nom de l'attraction
        :return: _nom
        """
        return f"Manège: {self._nom}"

    def arreter(self):
        """
        Méthode pour arrêter l'attraction
        :return: Print
        """
        super().arreter()
        if self.get_tourne():
            print("|-> le manège tourne bien...")


class MontagneRusse(Attraction):
    """
    Classe Montagne Russe
    """
    def __init__(self, nom, file, billet, places, vitesse_max):
        """
        Constructeur de la classe MontagneRusse (5 paramètres)
        :param nom: nom de l'attraction
        :param file: nombre de personnes dans la file d'attente
        :param billet: instance de la classe Billet
        :param places: places disponibles dans l'attraction
        :param vitesse_max: vitesse maximale de l'attraction
        """
        super().__init__(nom, file, billet, places)
        self._vitesse_max = vitesse_max

    def __str__(self):
        """
        Méthode pour afficher le nom de l'attraction
        :return: _nom
        """
        return f"Montagne russe: {self._nom}"


class Carrousel(Attraction):
    """
    Classe Carrousel
    """
    def __init__(self, nom, file, billet, places, hauteur):
        """
        Constructeur de la classe Carrousel (5 paramètres)
        :param nom: nom de l'attraction
        :param file: nombre de personnes dans la file d'attente
        :param billet: instance de la classe Billet
        :param places: places disponibles dans l'attraction
        :param hauteur: hauteur de l'attraction
        """
        super().__init__(nom, file, billet, places)
        self._hauteur = hauteur

    def __str__(self):
        """
        Méthode pour afficher le nom de l'attraction
        :return: _nom
        """
        return f"Carrousel: {self._nom}"


class Billet:
    """
    Classe Billet
    """
    id = 0

    def __init__(self, tarif):
        """
        Constructeur de la classe Billet (1 paramètre)
        :param tarif: tarif du billet
        """
        self._code = Billet.id
        self.date = datetime.datetime.now()
        self._tarif = tarif

        Billet.id += 1

    def get_tarif(self):
        """
        Méthode pour retourner le tarif du billet
        :return: _tarif
        """
        return self._tarif

    def __str__(self):
        """
        Méthode pour afficher le tarif du billet
        :return: {self._tarif}€
        """
        return f"{self._tarif}€"


if __name__ == '__main__':
    """
    Programme principal
    """
    parc = Parc("Parc d'attractions")
    attraction1 = Manege("Manège 1", 10, Billet(5), 20, 10)
    attraction2 = MontagneRusse("Montagne russe 1", 5, Billet(10), 15, 50)
    attraction3 = Carrousel("Carrousel 1", 15, Billet(3), 30, 5)
    parc.ajouter_attraction(attraction1)
    parc.ajouter_attraction(attraction2)
    parc.ajouter_attraction(attraction3)
    parc.vendre_entree(attraction1)
    parc.vendre_entree(attraction2)
    print_with_sep(parc)
    print_with_sep(attraction1)
    print_with_sep(attraction2)
    print_with_sep(attraction3)
    attraction1.afficher_statut()
    attraction2.afficher_statut()
    attraction3.afficher_statut()
    attraction3.reduire_file(5)
    attraction3.afficher_statut()
    attraction2.demarrer()
    attraction2.arreter()
    attraction3.arret_urgence()
    attraction1.set_tourne(True)
    attraction1.arreter()
    parc.desactiver_attraction(attraction1)
    parc.vendre_entree(attraction1)
    parc.vendre_entree(attraction2)
    parc.vendre_entree(attraction3)
    print_with_sep(parc)

# Date: 2024-04-10
# By: Corentin Lallement
# Github: https://github.com/CorentinL5/
# Last Run: 2024-04-10 20:18:07.357932
# Version: 1.0.0
# Status: finished
# Docs: 100% (docstrings)



