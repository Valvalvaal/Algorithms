# Binary search

#  


# Find First/Last Occurrence
def bin_search_first(arr, item):
    l = 0
    r = len(arr) -1
    first_occ = -1

    while l <= r:
        mid = (l + r) // 2
        guess = arr[mid]
        first_occ = -1

        if guess == item:
            # If we're looking for first occurence,
            # keep searching backwards, save least idx
            first_occ = mid
            r = mid - 1
        elif guess < item:
            l = mid + 1
        elif guess > item:
            r = mid - 1

        return first_occ
    
    arr = [1, 2, 2, 2, 3]
    print(bin_search_first(arr, 2))  # should print 1
    print(bin_search_first(arr, 3))  # should print 4
    print(bin_search_first(arr, 5))  # should print -1



# 11 Jun attempt // If not found, return pos where it should be
def bin_search_insert(arr, item):
    l = 0
    r = len(arr) - 1

    while l <= r:
        mid = (l + r) // 2
        guess = arr[mid]

        if guess == item:
            return mid
        elif guess < item:
            l = mid + 1
        else:
            r = mid - 1

    return l


def bin_search(arr: list, item: int) -> int:
    # We keep track of the left and right indices and the middle
    # index to chech whether that's the number we're looking for
    # returns the index where item is found else, returns -1
    l = 0
    r = len(arr) - 1

    while l <= r:
        mid = (l + r) // 2
        guess = arr[mid]

        if guess == item:
            return mid
        elif guess > item:
            r = mid - 1
        else:
            l = mid + 1

    return -1

# Test cases
print(bin_search([1,2,3,4,5,7,8,56,49], 3))
assert bin_search([1,2,3,4,5,7,8,56,49], 3) == 2