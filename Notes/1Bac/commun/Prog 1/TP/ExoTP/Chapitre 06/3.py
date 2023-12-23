# Page 153
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
lst_copy = []
for element in my_list:
    if not (element in lst_copy):
        lst_copy.append(element)
        

print("The list with unique elements only:")
print(lst_copy)