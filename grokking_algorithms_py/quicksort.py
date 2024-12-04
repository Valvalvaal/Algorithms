def qsort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
    return qsort(less) + [pivot] + qsort(greater)


print(qsort([7, 90, 8, 5, 3, 1, 60]))

# Quicksort in place, no additional space
def qsort2(array, left, right):
    if left >= right: 
        return
    partition_pos = partition(array, left, right) # final position of pivot
    qsort2(array, left, partition_pos - 1)
    qsort2(array, partition_pos + 1, right)

def partition(array, left, right):
    i = left
    j = right - 1
    pivot = array[right]

    while i < j:
        while i < right and array[i] < pivot:
            i += 1
        while j > left and array[j] > pivot:
            j -= 1
        if i < j:
            array[i], array[j] = array[j], array[i]

    if array[i] > pivot:
        array[i], array[right] = array[right], array[i]

    return i 

arr = [7, 90, 8, 5, 3, 1, 60]
qsort2(arr, 0, len(arr)-1)
print(arr)