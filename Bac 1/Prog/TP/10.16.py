x = input("entrer un phrase: ")

def conversoin(x):
    res = ''
    for char in x:
        if ord(char) <91:
            res += chr(ord(char)+32) 
        else:
            res += chr(ord(char)-32)
            
    print (res)

if __name__ == "__main__":
    conversoin(x)