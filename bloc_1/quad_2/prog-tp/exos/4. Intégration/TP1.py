class Vehicule:
    def __init__(self, identifiant, marque, modèle, année, kilometrage, tarif_journalier):
        self.__id = identifiant
        self.__marque = marque
        self.__modèle = modèle
        self.__année = année
        self.__kilometrage = kilometrage
        self.__tarif_journalier = tarif_journalier

    def __str__(self):
        return "{} : {} {} {} ({} $/jour)".format(self.__id, self.__marque, self.__modèle, self.__année, self.__tarif_journalier)

    def check_odometer(self):
        return self.kilometrage


class Voiture(Vehicule):
    def __init__(self, id, make, modèle, année, tarif_journalier, nbr_portes, vitesse_max):
        super().__init__(id, make, modèle, année, tarif_journalier)
        self.__nombre_portes = nbr_portes
        self.__vitesse_max = vitesse_max

    def __str__(self):
        return "Voiture : {} {} {} ({} $/jour)".format(self.__marque, self.__modèle, self.__année, self.__tarif_journalier)


class Camion(Vehicule):
    def __init__(self, id, make, model, year, tarif_journalier, payload_capacity, num_axles):
        super().__init__(id, make, model, year, tarif_journalier)
        self.__capacité_de_charge = payload_capacity
        self.__nombre_d_axles = num_axles

    def __str__(self):
        return "Camion : {} {} {} ({} $/jour)".format(self.__marque, self.__modèle, self.__année, self.__tarif_journalier)


class ContratLocation:
    def __init__(self, véhicule, date_début, date_fin, tarif_journalier):
        self.__véhicule = véhicule
        self.__date_début = date_début
        self.__date_fin = date_fin
        self.__tarif_journalier = tarif_journalier

    def coût_total(self):
        return (self.date_fin - self.date_début) * self.tarif_journalier


class SystèmeLocation:
    def __init__(self):
        self.__véhicules = []
        self.__contrats = []

    def ajouter_véhicule(self, véhicule):
        self.__véhicules.append(véhicule)

    def supprimer_véhicule(self, véhicule):
        self.__véhicules.remove(véhicule)

    def lister_véhicules(self):
        for véhicule in self.__véhicules:
            print(véhicule)

    def créer_contrat(self, véhicule, date_début, date_fin, tarif_journalier):
        contrat = ContratLocation(
            véhicule, date_début, date_fin, tarif_journalier)
        self.__contrats.append(contrat)

    def lister_contrats(self):
        for contrat in self.__contrats:
            print(contrat)

    def rendre_véhicule(self, véhicule):
        # J'ai pas compris
        pass
