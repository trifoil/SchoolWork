x = input("veuillez entrer un mot: ")
z=""
a=0
while(a<len(x)):
    if((a+1)==len(x)):
        z+=x[a]
        a=+1
    else:
        z+=x[a]+"*"
        a+=1
print(z)  