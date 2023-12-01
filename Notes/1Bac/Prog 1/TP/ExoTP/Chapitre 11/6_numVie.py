def lifeNum(date):
    while True:
        nbr = 0
        for i in str(date):
            nbr += int(i)

        if nbr < 10:
            break
        else:
            date = nbr

    return nbr


while True:
    try:
        dateIn = int(input("Date (AAAMMJJ) : "))
    except ValueError:
        print("Mauvais format")
    else:
        print("Numéro", lifeNum(dateIn))
        break



