# T: O(n), S: O(1)
def find_minimum(lst):
    if not lst:
        raise ValueError("List must not be empty")

    minimum = lst[0]
    for num in lst[1:]:
        if num < minimum:
            minimum = num
    return minimum