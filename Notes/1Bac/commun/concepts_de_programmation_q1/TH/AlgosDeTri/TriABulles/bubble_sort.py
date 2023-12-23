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