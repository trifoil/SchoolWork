# Page 269
def mysplit(strng):
    subStr = ''
    split = []

    for char in strng:
        # Si subStr n'est pas vide, ajouter à split
        if char == ' ':
            if subStr:
                split.append(subStr)
                subStr = ''

        else:
            subStr += char

    # Si subStr ne finit pas par un espace, le dernier mot ne s'ajoute pas
    # donc si c'est la cas, on ajoute manuellement le dernier mot
    if subStr:
        split.append(subStr)

    return split


print(mysplit("Être ou ne pas être, telle est la question"))
print(mysplit("Être ou ne pas être,telle est la question "))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
print(mysplit("Test   test    3456, aeaa"))
