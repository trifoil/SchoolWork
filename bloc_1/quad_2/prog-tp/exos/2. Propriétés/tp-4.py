class WeekDayError(Exception):
    def __init__(self, day):
        self.__msg = f"{day} n'est pas dans le liste des jours acceptés.\nJours acceptés : {Weeker.day}"
        super().__init__(self.__msg)


class Weeker:
    days = ["Lun", "Mar", "Mer", "Jeu", "Ven", "Sam", "Dim"]

    def __init__(self, day:str):
        if not day.lower().strip() in [x.lower() for x in Weeker.days]:
            raise WeekDayError(day=day)
        else:
            self.__day = day[0].upper() + day[1:].lower()

    def __str__(self):
        return self.__day

    def add_days(self, n: int):
        n %= 7
        day = (Weeker.days.index(self.__day) + n) % 7
        self.__day = Weeker.days[day]

    def subtract_days(self, n: int):
        n %= 7
        day = (Weeker.days.index(self.__day) - n) % 7
        self.__day = Weeker.days[day]

w = Weeker("Lun")
print(w)
w.add_days(15)
print(w, "-- Mar")
w.subtract_days(23)
print(w, "-- Dim")


