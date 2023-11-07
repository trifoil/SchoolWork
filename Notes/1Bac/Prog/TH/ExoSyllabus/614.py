l = ['Jean‐Michel', 'Marc', 'Vanessa', 'Anne', 'Maximilien',
'Alexandre‐Benoît', 'Louise']

out = []
    
for nom in l:
    tmp = nom + " " + str(len(nom))
    out.append(tmp)

print(out)
