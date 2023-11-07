t2 = ['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'Jean‐Pierre', 'Sandra']
grand = []
petit = []
for i in range(0, len(t2)):
  if len(t2[i]) < 6:
    petit.append(t2[i])
  elif len(t2[i]) >= 6:
    grand.append(t2[i])
  else:
    pass
print(grand)
print(petit)