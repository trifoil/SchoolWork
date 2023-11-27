# Page 187
def is_year_leap(year):
    bi = False

    if (year % 4 == 0):
        bi = True
        if (year % 100 == 0):
            bi = False
            if (year % 400 == 0):
                bi = True
    return bi


def days_in_month(year, month):
    l = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    if not (month in l):
        return None
    elif is_year_leap(year=year) and month == 2:
        return 29
    else:
        return l.get(month)


def day_of_year(year, month, day):
    day_dict = {
        0: "Lundi",
        1: "Mardi",
        2: "Mercredi",
        3: "Jeudi",
        4: "Vendredi",
        5: "Samedi",
        6: "Dimanche",

    }

    if (days_in_month(year=year, month=month) != day):
        return None

    d = day + (13*month-1)/5 + int(str(year)[-2:]) + int(
        str(year)[-2:])/4 + int(str(year)[:2])/4 - 2*int(str(year)[:2]
        )
    return day_dict.get(int(d % 7))


print(day_of_year(2000, 12, 31))
