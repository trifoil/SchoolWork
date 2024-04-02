class Robot:
    nombre_robots = 0
    
    def __init__(self, nom, batterie):
        self.__nom = nom
        Robot.__nombre_robots += 1
        self.__numero_serie = Robot.nombre_robots
        self.__batterie = batterie
        self.__x = 0
        self.__y = 0

    def __str__(self):
        return self.__nom + " n°" + str(self.__numero_serie) + " : " + str(self.__batterie) + "position : (" + str(self.__x) + ", " + str(self.__y) + ")"

    def seDeplacer(self, x, y):
        if self.__batterie >= 1:
            self.__x += x
            self.__y += y
        else:
            raise ValueError("La batterie n'est pas suffisante")

    def seRecharger(self):
        self.__batterie += 10

class Drone(Robot):
    def __init__(self, nom, batterie, portee_de_vol, camera_embarquee=False):
        super().__init__(nom, batterie)
        self.__portee_de_vol = portee_de_vol
        self.__camera_embarquee = camera_embarquee

    def volStationnaire(self, altitude):
        self.__portee_de_vol = altitude



class RobotDanseur(Robot):
    def __init__(self, nom, batterie, niveau_maitrise, partenaire=None, danses_connues=[]):
        super().__init__(nom, batterie)
        self.__niveau_maitrise = niveau_maitrise
        self.__partenaire = partenaire
        self.__danses_connues = danses_connues
    
    def danser(self, other, danse):
        if danse in self.danses_connues and danse in other.danses_connues:
            self.__partenaire = other
        else:
            raise ValueError("La danse n'est pas connue par un des robots")
        
    @property
    def danses_connues(self):
        return self.__danses_connues
    

