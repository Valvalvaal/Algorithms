def qsort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
    return qsort(less) + [pivot] + qsort(greater)

print(qsort([7,90,8,5,3,1,60]))
