t2 = [32, 5, 12, 8, 3, 75, 2, 15]
odd = []
even = []
for i in range(0, len(t2)):
    if t2[i] % 2 == 0:
        even.append(t2[i])
    else:
        odd.append(t2[i])

print(odd)
print(even)
