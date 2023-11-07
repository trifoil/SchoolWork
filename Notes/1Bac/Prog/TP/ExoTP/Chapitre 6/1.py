#Page 134
hat_list = list(range(1, 6))

# remplacer le numéro du
# milieu de la liste par un nombre entier entré par l’utilisateur
user_in = int(input("Numéro à insérer au milieu : "))
hat_list[2] = user_in

# écrire une ligne de code qui supprime le dernier élément de la liste 
hat_list.pop()

# écrire une ligne de code qui imprime la longueur de la liste existante 
print("Taille de la liste",len(hat_list))
print(hat_list)