conversion = input("1. °C -> F°\n2. °F -> C°\n>> ")

if(conversion == "1"):
    tempC = float(input("Température en °C : "))
    print(tempC * 1.8 + 32, "°F")
elif(conversion == "2"):
    tempF = float(input("Température en °F : "))
    print("%.2f °C" % ((tempF - 32) / 1.8))
else:
    print("Mauvais choix.")
