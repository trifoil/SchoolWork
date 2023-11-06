# Page 140
# step 1
groupes = []
print("Step 1:", groupes)


# step 2
groupes.append("Johan le Preteur")
groupes.append("Denis seins doux")
groupes.append("Yoan l'imprononçable")
print("Step 2:", groupes)


# step 3
user_in = input("Veillez ajouter le groupe 'Joakim Synagogue' : ")
groupes.append(user_in)
user_in = input("Veillez ajouter le groupe 'David Art Nouveau' : ")
groupes.append(user_in)
print("Step 3:", groupes)


# step 4
del groupes[4]
del groupes[3]
print("Step 4:", groupes)


# step 5
groupes.insert(0, "Erwin le schmet")
print("Step 5:", groupes)
# testing list legth
print("The Fab", len(groupes)) 