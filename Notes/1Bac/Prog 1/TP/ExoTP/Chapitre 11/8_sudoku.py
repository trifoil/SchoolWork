# Page 288
def checkSudo(sd):
    # Check line
    for line in sd:
        total = 45 # 1 + 2 + ... + 9 = 45
        for nb in line:
            total -= nb
        if total != 0:
            return False
    #Check col
    for col in range(9):
        total = 45
        for line in range(9):
            total -= sd[line][col]
        if total != 0:
            return False
    
    # Check 3x3
    for v in range(3):
        vOffset = v * 3
        for h in range(3):
            hOffset = h * 3
            total = 45
            #Subgrid check
            for i in range(3):
                for j in range(3):
                    total -= sd[i + hOffset][j + vOffset]

            if total != 0:
                return False

    return True






sudo = [
"195743862",
"431865927", 
"876192543", 
"387459216", 
"612387495", 
"549216738", 
"763524189", 
"928671354", 
"254938671",
]
print(checkSudo([[int(x) for x in sudo[i]] for i in range(9)]))

# while True:
#     for i in range(9):
#         try:
#             line = int(input("Rangée {}".format(i+1)))
#             if len(str(line)) < 2:
#                 raise Exception()
#         except ValueError:
#             print("Mauvais format")
#         else:
#             sudo.append([*str(line)])

