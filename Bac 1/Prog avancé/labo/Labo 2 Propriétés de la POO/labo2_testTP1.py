from labo2_TP1 import*

ma_voiture = Voiture(marque="Mercédes",modele="blabla",annee=2002,couleur="rouge",kilometrage=10)
ma_voiture2 = Voiture(marque="Mercédes",modele="blabla",annee=2002,couleur="rouge",kilometrage=10)
ma_voiture.changer_couleur("blanc")
ma_voiture2.changer_couleur("vert")
ma_voiture.afficher_informations()
print(ma_voiture.__dict__)
print(ma_voiture2.__dict__)
ma_voiture2.afficher_informations()