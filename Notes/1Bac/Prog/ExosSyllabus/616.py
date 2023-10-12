m = 10000*10000
cst = 6.67*10**-11
d = 0.05

while(True):
    print("d=",d,"m : la force vaut", "%.4f" % (cst*(m/d**2)), "N")
    d = d * 2
    n = input("")
    
    if(n != ""):
        break