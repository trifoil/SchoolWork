# 327
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

    out = sorted(lettersDict.items(), key=lambda x: x[1], reverse=True)

    with open("a.hist", 'w+') as f:
        for i in out:
            j = f"{i[0]} {i[1]}\n"
            f.write(j)


while True:
    fichier = input("Entrez le nom du fichier du prof : ")
    try:
        stream = open(fichier, "r", encoding='UTF-8')
    except IOError as err:
        print(err)
    else:
        break

lettersCount(stream)
