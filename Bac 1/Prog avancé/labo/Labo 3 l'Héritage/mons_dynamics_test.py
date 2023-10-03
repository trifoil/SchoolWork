from mons_dynamics import *

Marcel = Drone(portee_de_vol=2,camera_enbarque="oui",batterie=0)
Marcel.se_deplacer("nord")
Marcel.vol_stationnaire(10)
Marcel.se_recharger()




Arnaud = Robot_Danceur(niveau_de_maitrise="infini",partenaire="Marcel2",danses="macaréna",batterie=0)
Marcel2 = Robot_Danceur(niveau_de_maitrise="10",partenaire="Arnaud",danses="macaréna",batterie=10)
Arnaud.danser(Arnaud,"macaréna")
Arnaud.se_deplacer("nord")

Arnaud.se_recharger()