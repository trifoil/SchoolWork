from labo3_TP1 import *

Marcel = Moldu(nom="Marcel",prenom="Marcel",annee_de_naissance=2000, travail="mineur",connaissance_de_la_magie=False)

Marcel.calculer_age()
print(Marcel.sePresenter())

Marcel = Sorcier(nom="Marcel",prenom="Alexandre",annee_de_naissance=2000,baguette="clope",maison="Poufsouffle")
print(Marcel.SePresenter())