def heapify(arr, lenght, node, condition):
    new_node = node
    left = 2*node+1
    right = 2*node+2

    if left < lenght and condition(arr[new_node], arr[left]):
        new_node = left

    if right < lenght and condition(arr[new_node], arr[right]):
        new_node = right

    if new_node != node:
        arr[node], arr[new_node] = arr[new_node], arr[node]
        heapify(arr, lenght, new_node, condition)


def heap_sort(arr, condition):
    lenght = len(arr)

    for i in range(lenght // 2, -1, -1):
        heapify(arr, lenght, i, condition)
    
    for i in range(lenght-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0, condition)


def condition(element_1, element_2):
    return element_1 <= element_2


my_list = [9, 4, 3, 2, 6, 5, 234, 2.5, -1, 666, 69]
heap_sort(my_list, condition)
print(my_list)