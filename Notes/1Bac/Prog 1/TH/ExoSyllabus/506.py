string = input("Chaine : ")
cond = False
for i in range(0, len(string)):
    if string[i].lower() == 'e':
        cond = not cond
        break
print(cond)
