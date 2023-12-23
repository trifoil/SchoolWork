# Page 283
msg = input("Message : ")

while True:
    try:
        decalage = int(input("Décalage (entre 1 et 25) : "))
        if not decalage in range(1,26):
            raise Exception()
    except ValueError:
        pass
    else:
        break

for letter in msg:
    if letter.isalpha():

        if letter.islower():
            letter_dec = ord(letter) + decalage
            if letter_dec > 122:
                letter_dec -= 26
        
        if letter.isupper():
            letter_dec = ord(letter) + decalage
            if letter_dec > 90:
                letter_dec -= 26
        
        print(chr(letter_dec), end="")
    
    else:
        print(letter, end='')

