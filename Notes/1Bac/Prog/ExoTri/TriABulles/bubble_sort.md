## Exo

Algorithme de tri à bulles

Faire :
- Déroulement en français.
- Arbre algorithmique ou Pseudo-code.
- Code Python (Itératif).

### Français

1. On parcourt la liste à partir de la droite autant de fois qu'il y a d'éléments dans la liste.
2. À chaque fois, on compare l'élément avec celui à sa gauche. Si la condition du tri est fausse, on les inverse.
3. À chaque étape, on sait qu'un élément à l'extrême gauche en plus est à la bonne position. On ne le prendra plus en compte dans les prochaines itérations.

### Pseudo Code.

```txt
tempon;

pour int i = 1; i < taille list; i++
    pour int transmutation = taille de list - 1; transmutation > i; transmutation--
        tempon = élément transmutation de list
        si la condition entre l'élément et son voisin de gauche est vraie
            élément transmutation de list = élément transmutation - 1 de list
            élément transmutation de list - 1 de list = tempon
```

### Code python

Base:
```py
def bubble_sort(list, condition):
    # bubble sort code


def condition(element_1, element_2):
    return element_1 <= element_2


my_list = [1, 4, 3, 2, 6, 5]
bubble_sort(my_list, condition)
print(my_list)
```

Answer:
```py
def bubble_sort(list, condition):
    tempon = 0
    for i in range(len(list)):
        for j in range(len(list) - 1, i, -1):
            tempon = list[j]
            if condition(tempon, list[j - 1]):
                list[j] = list[j - 1]
                list[j - 1] = tempon


def condition(element_1, element_2):
    return element_1 <= element_2


my_list = [1, 4, 3, 2, 6, 5]
bubble_sort(my_list, condition)
print(my_list)
```