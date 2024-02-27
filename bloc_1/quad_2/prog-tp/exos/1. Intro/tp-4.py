import random

class d6:
    def __init__(self):
        self.__valeur = None
        self.lancerDe()

    def lancerDe(self):
        self.__valeur = random.randrange(1, 7)

    @property
    def valeur(self):
        return self.__valeur
        
dé1 = d6()
dé2 = d6()
dé3 = d6()
dé4 = d6()
dé5 = d6()

while True:
    res = 0
    res += dé1.valeur
    res += dé2.valeur
    res += dé3.valeur
    res += dé3.valeur
    res += dé5.valeur
    print(res)
    if not (res < 24):
        break
    dé1.lancerDe()
    dé2.lancerDe()
    dé3.lancerDe()
    dé4.lancerDe()
    dé5.lancerDe()


