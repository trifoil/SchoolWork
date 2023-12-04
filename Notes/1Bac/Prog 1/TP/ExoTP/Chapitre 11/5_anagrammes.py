# Page 285

def agrammes(word1, word2):
    word1 = "".join(word1.split()).lower()
    word2 = "".join(word2.split()).lower()
    word2 = [*word2]

    if len(word1) != len(word2) or (len(word1) and len(word2)) == 0:
        return False
    
    for i in word1:
        if i in word2:
            word2.remove(i)
        else:
            return False
    return True


first_word = input("Premier mot : ")
seconde_word = input("Deuxième mot : ")

if agrammes(first_word, seconde_word):
    print("Anagrammes")
else:
    print("Pas d'anagrammes")