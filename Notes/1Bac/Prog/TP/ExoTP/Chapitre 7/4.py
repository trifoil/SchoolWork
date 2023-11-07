# Page 188
from math import sqrt


def is_prime(a):
    for i in range(2, a):
        if i > sqrt(a):
            break
        if a % i == 0:
            return False

    if a == 0 or a == 1:
        return False
    else:
        return True
for i in range(2, 100):
    if is_prime(i):
        print(i)

