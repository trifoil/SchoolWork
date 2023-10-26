def maximum(n1,n2,n3):
    lst = []
    lst.append(n1)
    lst.append(n2)
    lst.append(n3)
    lst.sort()
    return lst[2]

print(maximum(2,5,4))