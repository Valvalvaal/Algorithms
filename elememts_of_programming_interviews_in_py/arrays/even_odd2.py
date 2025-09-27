# T: O(N), S: O(1)

# My solution uses 3 imaginary arrays to sort the input array in place.
# The 3 sub-arrays are Even, Unclassified and Odd. We use two pointers
# to keep track of the boundaries of these sub-arrays and move them.

def even_odd1(arr):
    # pointers to keep track of the end of the even array and start of 
    # the odd one.
    even_end, odd_start = 0, len(arr) - 1

    # Keep checking until all nums have been validated, until pointers
    # cross paths
    while even_end < odd_start:
        # If odd, shift with num at odd_start and grow the odd sub array
        if arr[even_end] % 2 != 0:
            arr[even_end], arr[odd_start] = arr[odd_start], arr[even_end]
            odd_start -= 1
        else:
            even_end += 1
    
    return arr

# Test Cases
def test_even_odd1():

    # Edge Cases
    assert even_odd1([0]) == [0] # Single even
    assert even_odd1([1]) == [1] # Single odd
    assert even_odd1([]) == [] # Empty

    # All even
    assert even_odd1([2,4,8,10]) == [2,4,8,10]

    # All odd
    assert set(even_odd1([1,3,11,1])) == {1,3,11,1}
    
    # Mixed small case
    arr = [1, 2, 3, 4]
    result = even_odd1(arr[:])
    assert set(result) == {1, 2, 3, 4}
    assert all(x % 2 == 0 for x in result[:2])
    assert all(x % 2 == 1 for x in result[2:])

    print("All tests passed ✅")

test_even_odd1()
            
