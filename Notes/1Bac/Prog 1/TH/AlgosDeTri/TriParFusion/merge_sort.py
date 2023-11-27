#https://www.youtube.com/watch?v=cVZMah9kEjI
from random import randint


def randomList():
    lst = []
    for i in range(0, randint(15,30)):
        lst.append(randint(0,100))
    return lst


def mergeSort(tab):
    if len(tab) > 1:
        # Divise la liste en 2 
        left = tab[:len(tab)//2]
        right = tab[len(tab)//2:]
        
        # Recursion
        mergeSort(left)
        mergeSort(right)
        
        # Merge
        i = 0 
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                tab[k] = left[i]
                i += 1
            else:
                tab[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            tab[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            tab[k] = right[j]
            j += 1
            k += 1

liste = randomList()
mergeSort(liste)
print(liste)