# Optimized T: O(n), S:O(1)
def find_second_maximum2(nums):
    maximum = second_maximum = float('-inf')

    for num in nums:
        if num > maximum:
            maximum, second_maximum = num, maximum
        # Handle case of decreasing sequence or same elems
        elif num < maximum and num > second_maximum:
            second_maximum = num

    return None if second_maximum == float('-inf') else second_maximum
        
# Test Cases

assert find_second_maximum2([4, 2, 1, 5, 0]) == 4 # Regular case
assert find_second_maximum2([4, -2]) == -2 # only two elems
assert find_second_maximum2([4, 4]) == None # same elems        

# T: O(n), S:O(1)
def find_second_maximum(nums):
    # Idea: Traverse the array once, keeping a similar ds to a 
    # stack of size two where I can peek the top item, if there's 
    # something greater we push elem to the stack and eliminate the
    # third elem to keep just two elements

    # [4, 2, 1, 5, 0], aux = [4, 2] start ordered aux ds
    #              p
    # p -> 1, compare to aux[0] = 4, 1 < aux[0], p++
    # p -> 5, 5 > aux[0] = 4, push 5 into aux -> aux = [5, 4], p++
    # p -> 0, compare to aux[0] = 5, 0 < aux[0], p++
    # end p = len(nums)

    two_maximum = [0, 0]
    two_maximum[0] = nums[0] if nums[0] > nums[1] else nums[1]
    two_maximum[1] = nums[0] if nums[0] <= nums[1] else nums[1]

    for curr in nums[2:]:
        if curr > two_maximum[0]:
            two_maximum[1] = two_maximum[0]
            two_maximum[0] = curr

    return two_maximum[1]    


# Test Cases

assert find_second_maximum([4, 2, 1, 5, 0]) == 4 # Regular case
assert find_second_maximum([4, -2]) == -2 # only two elems
assert find_second_maximum([4, 4]) == 4 # same elems
