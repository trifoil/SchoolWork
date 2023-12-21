# 328
def moyenne(file):
    dictStudents = {}

    for line in file:
        sl = line.split()
        name = f"{sl[0]} {sl[1]}"
        sl[2] = float(sl[2].replace(',', '.'))

        if name not in dictStudents:
            dictStudents[name] = [sl[2], 1]
        else:
            dictStudents[name][0] += sl[2]
            dictStudents[name][1] += 1

    # écriture dans le fichier
    with open("rapport.txt", 'w+') as f:
        for name, (total, count) in dictStudents.items():
            average = total / count
            prt = name + " " + str(average) + "\n"
            f.write(prt)


while True:
    fichier = input("Entrez le nom du fichier : ")
    try:
        stream = open(fichier, "r", encoding='UTF-8')
    except IOError as err:
        print(err)
    else:
        break

moyenne(stream)
