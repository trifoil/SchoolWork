def nomMois(n):
    mois = {
        1 : "Janvier",
        2 : "Février",
        3 : "Mars",
        4 : "Avril",
        5 : "Mai",
        6 : "Juin",
        7 : "Juillet",
        8 : "Août",
        9 : "Septembre",
        10 : "Octobre",
        11 : "Novembre",
        12 : "Décembre"
    }
    if (n in mois):
        return mois.get(n)
    else:
        return None
    
print(nomMois(12))