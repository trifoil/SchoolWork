# Page 284 
userIn = "La mariée ira mal"

def accent(ch):
    letters = {
        "é": "e",
        "è": "e",
        "à": "a",
        "ù": "u",
        "â": "a",
        "ê": "e",
        "î": "i",
        "ô": "o",
        "û": "u"
    }
    if letters.get(ch):
        return letters[ch]
    else:
        return ch


def palindrome(strg):
    strg = "".join(strg.split()).lower()


    for i in range(0, len(strg)):
        if not accent(strg[i]) == accent(strg[(len(strg)- 1) - i]):
            print("Pas palindorme")
            return False
    
    print("Palindrome")
    return True

palindrome(userIn)
    