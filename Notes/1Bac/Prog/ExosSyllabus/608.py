a = int(input("Borne a : "))
b = int(input("Borne b : "))
cnt = a
total = 0

if a>=b:
    print('borne a trop grande ')
else:
    while(cnt<=b):
        if((cnt % 3) == 0 and (cnt % 5) == 0 ):
            total += cnt
        cnt += 1

print(total)