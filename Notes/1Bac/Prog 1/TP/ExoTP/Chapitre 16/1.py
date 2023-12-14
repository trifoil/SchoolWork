# 326
def lettersCount(str):
    lettersDict = {}
    for ch in str.read():
        ch = ch.lower()
        
        if not ch.isalnum():
            continue
        if not ch in lettersDict.keys():
            lettersDict[ch] = 1
        else:
            lettersDict[ch] += 1

    orderedList = list(lettersDict.keys())
    orderedList.sort()
    
    for l in orderedList:
        print(l, lettersDict[l])


while True:
    fichier = input("Entrez le nom du fichier : ")
    try:
        stream = open(fichier, "r", encoding='UTF-8')
    except IOError as err:
        print(err)
    else:
        break

lettersCount(stream)