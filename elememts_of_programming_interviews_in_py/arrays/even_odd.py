# Reorder the input array so that the even entries appear first. 
# Solve in O(1) space

def even_odd2(A):
    next_even, next_odd = 0, len(A) - 1
    if next_even % 2 == 0:
        next_even += 1
    else:
        A[next_even], A[next_odd] = A[next_odd], A[next_even] 
        next_odd -= 1
    return A

# T: O(N), S: O(1)
def even_odd(A):
    # With arrays is easy to operate on both ends
    # Here we partition the array into 3 sub-arrays in the order:
    # Even, Unclassified, Odd. We use two pointers and move them 
    # closer by classifing and emptying the Unclassified arr nums.
    next_even, next_odd = 0, len(A) - 1

    while next_even < next_odd:
        # Grow even sub-array if A[next_even] is even
        if A[next_even] % 2 == 0:
            next_even += 1
        else:
            # Grow odd sub-array by trading the reviewed odd num by 
            # the not yet reviewed num in the Unclassified sub-arr
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            next_odd -= 1

# Test Cases
arr = [2,5,6,7,7,777,8,1,2,34,5,80,66,3,77,98,8,7,68,8]
even_odd(arr)
assert arr == [2, 8, 6, 68, 8, 98, 8, 66, 2, 34, 80, 5, 3, 77, 1, 777, 7, 7, 7, 5], \
    f"not correctly sorted, got: {arr}"
print(even_odd2(arr))
