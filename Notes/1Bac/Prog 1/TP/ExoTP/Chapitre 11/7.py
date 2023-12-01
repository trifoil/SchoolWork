# Page 287

def charIn(w1, w2):
    w1 = [*w1.lower()]
    w2 = [*w2.lower()]
    
    for i in w1:
        if not i in w2:
            return False
        w2.remove(i)

    return True

try:
    word1 = input("Première chaîne : ")
    word2 = input("Deuxième chaîne : ")
    word1 = "dons"
    word2 = "Nabuchodonosor"
except:
    pass
else:
    if charIn(word1, word2):
        print("Oui")
    else:
        print("Non")