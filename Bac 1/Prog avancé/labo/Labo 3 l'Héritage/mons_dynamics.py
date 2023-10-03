class Robot:
    nombre_de_robot = 0
    def __init__(self,batterie):
        
        self._batterie = batterie
        Robot.nombre_de_robot+=1
        self._numero_de_serie = Robot.nombre_de_robot

    def se_recharger(self):
        if self._batterie <=100:
            if self._batterie <=90 :
                self._batterie+=10
                print(self._batterie)
            else :
                self._batterie =100
                print(self._batterie)
        else : 
            print("impossible d'avoir + de 100% ")

class Drone(Robot):
    def __init__(self,portee_de_vol,camera_enbarque,batterie):
        self._portee_de_vol = portee_de_vol
        self._camera_embarque= camera_enbarque
        super().__init__(batterie)

    def se_deplacer(self,direction):
        if self._batterie >=0:
            print(f"le robot se déplace dans la direction {direction} en volant ")
        else:
            print("plus de batterie")

    def vol_stationnaire(self,altitude):
        if self._batterie>0:
            print(f"Le drône est en vol stationaire et vole a {altitude} m")
        else: 
            print("le drone c'est écrasé au sol parce qu'il n'avait plus de batterie")
    def __str__(self):
        return f"Drone {self._numero_de_serie} a une portée de vol de {self._portee_de_vol},a une pourcentage de batterie de {self._batterie} et possède une caméra embarque ? {self._camera_embarque} "
        
class Robot_Danceur(Robot):
    def __init__(self,niveau_de_maitrise,partenaire,danses,batterie):
        self._niveau_de_maitrise = niveau_de_maitrise
        self._partenaire = partenaire
        self._danses = danses
        super().__init__(batterie)
        
    def se_deplacer(self,direction):
        if self._batterie>0:
            print(f"le robot se déplace dans la direction {direction} en dansant")
        else:
            print("plus de batterie")

    def danser(self,partenaire,une_danse):
        if self._batterie>0:
            if une_danse in self._danses:
                print(f"le robot danceur danse {une_danse} avec {partenaire}")
            else :
                print("il n'a pas cette danse")
        else:
            print("plus de batterie")

    def __str__(self):
        return f"Robot danceurs {self._numero_de_serie} a une niveau de maitrise {self._niveau_de_maitrise}, a comme partenaire{self._partenaire}, sais danser{self._danses} et a un pourcentage de batterie{self._batterie}"