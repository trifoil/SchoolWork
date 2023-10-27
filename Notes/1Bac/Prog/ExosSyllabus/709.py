def compteCar(ca,ch):
    cnt = 0
    for letter in ch:
        if letter == ca:
            cnt += 1
    return cnt

print(compteCar('e', 'Cette phrase est un exemple'))