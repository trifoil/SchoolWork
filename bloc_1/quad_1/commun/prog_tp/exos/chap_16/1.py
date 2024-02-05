# 326
def lettersCount(input_str):
    lettersDict = {}
    for ch in input_str.read():
        ch = ch.lower()
        
        if not ch.isalnum():
            continue
        if not ch in lettersDict:
            lettersDict[ch] = 1
        else:
            lettersDict[ch] += 1

    orderedList = list(lettersDict.keys())
    orderedList.sort()
    
    with open("a.hist", 'w+') as f:
        for l in orderedList:
            prt = f"{l} {lettersDict[l]}\n"
            f.write(prt)




while True:
    fichier = input("Entrez le nom du fichier : ")
    try:
        stream = open(fichier, "r", encoding='UTF-8')
    except IOError as err:
        print(err)
    else:
        break

lettersCount(stream)