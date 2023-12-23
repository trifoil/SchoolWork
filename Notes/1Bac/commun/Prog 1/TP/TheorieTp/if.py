# Joue avec les valeur du dessous pour comprendre les 'if' ;)
condition, condition_2, condition_x = False, False, True

# if statement
if condition:
    print("Print ce texte si 'condition' est vraie")
elif condition_2:
    print("Print ce texte si 'condition' est fausse mais que 'condition_2' est vraie")
elif condition_x:
    print("On peut avoir autant de elif qu'on veut")
else:
    print("Print ce texte si aucune des conditions n'est vraie")
