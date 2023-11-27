string = input("Chaine : ")
cnt = 0
for i in range(0, len(string)):
    if string[i].lower() == 'e':
        cnt += 1
print(cnt)
