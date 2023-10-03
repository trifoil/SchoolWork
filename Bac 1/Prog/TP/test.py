def insertsort(array):
    for i in range(1,len(array)):
        key = array[i]
        j = i-1
        while j>=0 and key<array[j]:
            array[j+1]= array[j]
            j-=1
        array[j+1]= key

array = [1,3,2,9,2,8]
insertsort(array)
print(array)