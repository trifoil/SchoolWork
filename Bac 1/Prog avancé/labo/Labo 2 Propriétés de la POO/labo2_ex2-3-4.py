class Python :
    population = 1                # de classe
    victims = 0                   # de class
    def __init__(self):
        self.length_ft = 3        #d'instance
        self.__venomous = False   #privé et d'instance
        
version_2 = Python()
version_2._Python__venomous = True
print(version_2._Python__venomous)
print(hasattr(version_2,"constrictor"))
