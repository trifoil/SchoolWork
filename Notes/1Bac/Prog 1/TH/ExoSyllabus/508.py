string = input("Chaine : ")
newString = ""
for i in range(0, len(string)):
    newString += string[i] + '*'

newString = newString[:(len(newString) - 1)]
print(newString)
