class Timer:
    def __init__(self, heures=0, minutes=0, secondes=0):
        self.__heures = heures
        self.__minutes = minutes
        self.__secondes = secondes

    def __str__(self):
        h = self.__format(self.__heures)
        m = self.__format(self.__minutes)
        s = self.__format(self.__secondes)
        return f"{h}:{m}:{s}"
    
    def __format(self, x:int):
            if x < 10: 
                return "0" + str(x)
            else:
                return str(x)
    
    def next_second(self):
        self.__secondes = (self.__secondes + 1) % 60
        self.__minutes = (self.__minutes + (self.__secondes == 0)) % 60
        self.__heures = (self.__heures + (self.__minutes == 0 and self.__secondes == 0)) % 24
             

    def previous_second(self):
        self.__secondes = (self.__secondes - 1) % 60
        self.__minutes = (self.__minutes - (self.__secondes == 59)) % 60
        self.__heures = (self.__heures - (self.__minutes == 59 and self.__secondes == 59)) % 24

if __name__ == "__main__":
    timer1 = Timer(23, 59, 59)
    print(timer1)
    timer1.next_second()
    print(timer1)
    timer1.previous_second()
    print(timer1)
