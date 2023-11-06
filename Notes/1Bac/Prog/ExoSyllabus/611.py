a = int(input("Entrez la longueur du côté a : "))
b = int(input("Entrez la longueur du côté b : "))
c = int(input("Entrez la longueur du côté c : "))

# Inégalité triangulaire : |x + y| <= |x| + |y|
# AC <= AB + BC, si =, alors c'est une ligne donc
# donc si AC > BC et AC > AB, et AC < AB + BC, ABC = triangle

lst = [a, b, c]
lst.sort()

if lst[0]+lst[1] <= lst[2]:
    print("Impossible de former un triangle")
else:
    if(lst[0] == lst[1] == lst[2]):
        print("triangle équilatéral")
    elif (lst[0] == lst[1] or lst[1] == lst[2]):
        if ((lst[0] + lst[1])**2 == lst[2]**2):
            print("Triangle isocèle rectangle")
        else:
            print("Triangle isocèle")
    elif((lst[0] + lst[1])**2 == lst[2]**2):
        print("Triangle rectangle")
    else:
        print("Triangle quelconque")
        