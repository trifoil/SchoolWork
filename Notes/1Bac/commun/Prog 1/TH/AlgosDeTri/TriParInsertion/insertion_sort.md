# Insertion sort

## Exo

Algorithme de tri par insertion

Faire :
- Déroulement en français.
- Arbre algorithmique ou Pseudo-code.
- Code Python (itératif).


### Francais

1. Parcourir la liste à partir du deuxième élément de gauche autant de fois qu'il y a d'éléments dans la liste.
2. Stocker l'élément dans un tampon.
3. Comparer tous les éléments précédents avec notre élément, tant que la condition est vraie, les déplacer d'une position vers la droite.
4. Une fois que la condition devient fausse, placer notre tampon juste à droite de l'élément déclencheur.


### Pseudo Code.

```txt
tampon;
j;

pour i de 1 à taille de la liste faire
    tampon <- élément i de la liste
    j = i - 1
    tant que j >= 0 et que la condition entre l'élément i et l'élément j est vraie faire
        élément j + 1 de la liste = élément j de la liste
        j--
```

### Code python

Base:
```py
def insertion_sort(list, condtion):
    # insertion sort code


def condition(element_1, element_2):
    return element_1 <= element_2


my_list = [9, 4, 3, 2, 6, 5]
insertion_sort(my_list, condition)
print(my_list)
```

Answer:
```py
def insertion_sort(list, condition):
    tempon = 0
    j = 0
    for i in range(1, len(list)):
        tempon = list[i]
        j = i - 1
        while j >= 0 and condition(tempon, list[j]):
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = tempon


def condition(element_1, element_2):
    return element_1 <= element_2


my_list = [9, 4, 3, 2, 6, 5]
insertion_sort(my_list, condition)
print(my_list)
```