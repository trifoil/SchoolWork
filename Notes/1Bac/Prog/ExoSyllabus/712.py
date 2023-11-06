def inverse(ch):
    reverse = ""
    for i in range(len(ch) -1, -1, -1):
        reverse += ch[i]

    return reverse

print(inverse("banger"))