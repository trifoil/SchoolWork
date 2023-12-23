# Page 186
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

    if (month not in l):
        return None
    elif is_year_leap(year=year) and month == 2:
        return 29
    else:
        return l.get(month)


test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]

for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("KO")
