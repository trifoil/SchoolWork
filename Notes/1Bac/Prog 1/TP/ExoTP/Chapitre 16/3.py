# 328
def moyenne(file):
    dictStudents = {}
    l = file.readline()
    
    while l != '':
        sl = l.split()
        name = sl[0] + " " + sl[1]
        sl[2] = float(sl[2].replace(',', '.'))
        
        if not name in list(dictStudents.keys()):
            dictStudents[name] = [sl[2], 1]
        else:
            tmp = dictStudents[name]
            tmp[0] += sl[2]
            tmp[1] += 1 
            dictStudents[name] = tmp
        
        l = file.readline()
    
    for i in dictStudents.keys():
        note = dictStudents[i]
        note = note[0]/note[1]
        print(i, note)


while True:
    fichier = input("Entrez le nom du fichier : ")
    try:
        stream = open(fichier, "r", encoding='UTF-8')
    except IOError as err:
        print(err)
    else:
        break

moyenne(stream)
