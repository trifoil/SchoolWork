note = int(input="Note : ") 
sur = int(input("sur combien ? : "))

pourcentage = note/sur
if(pourcentage < 0.4):
    print("E")
if(0.4 <= pourcentage < 0.5):
    print("D")
if(0.5 <= pourcentage < 0.6):
    print("C")
if(0.6 <= pourcentage < 0.8):
    print("B")
if(0.8 <= pourcentage):
    print("A")

