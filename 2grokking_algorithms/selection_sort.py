# Selection Sort traverses through the arr looking for the smallest item
# then taks that item and organizes in the output array.

def find_smallest(arr):
    smallest = arr[0]
    smallest_idx = 0
    i = 1

    while i < len(arr):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_idx = i
        i += 1

    return smallest_idx

def selection_sort(arr):
    copy_arr = list(arr)
    sorted = []
    i = 0

    while i < len(arr):
        smallest_idx = find_smallest(copy_arr)
        sorted.append(copy_arr.pop(smallest_idx))
        i += 1
        
    return sorted

print(selection_sort([5, 3, 6, 2, 10]))