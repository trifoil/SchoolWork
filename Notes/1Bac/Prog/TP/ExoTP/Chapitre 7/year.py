# Résolution des exercices sous forme d'objet

class Year():
    """Objet Year
    """
    def __init__(self, valeur):
        self.valeur = int(valeur)
        self.bissextile = False
        self.is_year_leap()

    def is_year_leap(self):
        """Vérifie si une année est bissextile
        """
        if (self.valeur % 4 == 0):
            self.bissextile = True
            if (self.valeur % 100 == 0):
                self.bissextile = False
                if (self.valeur % 400 == 0):
                    self.bissextile = True
    
    def days_in_month(self, month):
        """Renvoie le nombre de jour dans un mois de l'année 

        Args:
            mois (int): Le mois, entre 1 et 12

        Returns:
            int: le nombre de jour dans le mois spécifié
            None: Si le mois n'est pas compris entre 1 et 12
        """
        month_dict = {
            1: 31,
            2: 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31
        }

        if (month not in month_dict):
            return None
        elif self.bissextile and month == 2:
            return 29
        else:
            return month_dict.get(month)

    def day_of_year(self, month, day):
        """Renvoie le nom du jour étant donné le mois et le jour

        Args:
            month (int)
            day (int)

        Returns:
            str: le nom du jour correspondant
            None: si l'argument day est trop grand
        """
        days_dict = {
            0: "Lundi",
            1: "Mardi",
            2: "Mercredi",
            3: "Jeudi",
            4: "Vendredi",
            5: "Samedi",
            6: "Dimanche",

        }

        if (self.days_in_month(month) != day):
            return None

        d = day + (13*month-1)/5 + int(str(self.valeur)[-2:]) + int(
            str(self.valeur)[-2:])/4 + int(str(self.valeur)[:2])/4 - 2*int(str(self.valeur)[:2])
        
        return days_dict.get(int(d % 7))
    
    def __str__(self):
        return str(self.valeur)
    
    def __len__(self):
        return self.valeur