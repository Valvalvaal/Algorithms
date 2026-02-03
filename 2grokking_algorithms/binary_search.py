# Binary search
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