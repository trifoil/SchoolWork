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