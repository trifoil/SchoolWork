def compte():
    file = open("test.txt","r")
    t = file.readlines()
    file.close()
    print(t)
    ch = ' '
    wordCount = 1
    for line in t:
        for char in line:
            if char == ch or char == '\n':
                wordCount += 1
    return wordCount
print(compte())
