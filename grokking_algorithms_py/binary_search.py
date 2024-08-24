# Tuesday 25 May

# Implementation of binary search algorithm 

def binary_search(sorted_array, item):
    """ 
    Parameters:
            sorted_array: Array 
            item: The number that we want to find
    Returns:
            item position
            or null if the item is not in the array
    Complexity:
            log(n), n: length of array
    """
    low = 0
    high = len(sorted_array)-1

    while low <= high:
        mid = (low + high)//2
        guess = sorted_array[mid]
        if guess == item:
            return mid
        elif item > guess:
            low = mid + 1 
        else:
            high = mid - 1
    return None

my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3)) # => 1
print(binary_search(my_list, 9)) # => 4
