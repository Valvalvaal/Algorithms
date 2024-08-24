# Thursday 27 May

# Implementation of selection sort algorithm

def find_smallest(arr):
    position_smallest = 0
    smallest = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            position_smallest = i
    return position_smallest

def selection_sort(arr):
    sorted_arr = []
    while len(arr):
        position_smallest = find_smallest(arr)
        sorted_arr.append(arr.pop(position_smallest))
    return sorted_arr

# Test
print(selection_sort([0,-9,70,9,4,3,101,7,5,2,2,6,100,-3]))
        