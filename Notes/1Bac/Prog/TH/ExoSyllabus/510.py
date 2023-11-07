string = input("Chaine : ")
newString = ""
for i in range(len(string) -1 , -1, -1):
    newString += string[i]

print(string == newString)
