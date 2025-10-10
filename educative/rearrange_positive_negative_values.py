# T: O(n), S: O(1)

def rearrange2(nums):
    neg_index = 0

    for i in range(len(nums)):
        if nums[i] < 0:
            nums[i], nums[neg_index] = nums[neg_index], nums[i]
            neg_index += 1

    return nums

# Test cases
assert rearrange2([5, 8, -2, -2, 6, -4]) == [-2, -2, -4, 8, 6, 5]
assert rearrange2([-4, -2, -2]) == [-4, -2, -2] # All negative
assert rearrange2([4, 2, 2]) == [4, 2, 2] # All positive

# T: O(n/2) = O(n), S: O(1)

# Idea: Sort list in-place by using two pointers to keep track of two
# imaginary sub lists: [negative, unordered, positive]. The two pointers
# negative points to the end of the first sub list, positive to the beginning 
# of the last sublist. In each step of the iteration, grow each array if we find
# a num that corresponds

# [5, 8, -2, -2, 6, -4]
# n                   p, nums[n] > 0, shift(nums[n], nums[p]), grow positive list, p--
# [-4, 8, -2, -2, 6, 5]
#  n              p    , nums[n] < 0, grow negative list, n++
# [-4, 8, -2, -2, 6, 5]
#      n          p    , nums[n] > 0, shift(nums[n], nums[p]), p--
# [-4, 6, -2, -2, 8, 5] 
#      n       p       , nums[0] > 0, shift(nums[n], nums[p]), p--
# [-4, -2, -2, 6, 8, 5]    
#      n    p          , nums[0] < 0, n++
# [-4, -2, -2, 6, 8, 5]  -> n == p we stop, the unordered sublist in now empty  

def rearrange(nums):
    neg_end = 0
    pos_start = len(nums) - 1

    while neg_end < pos_start:
        if nums[neg_end] < 0:
            neg_end += 1
        else:
            nums[neg_end], nums[pos_start] = nums[pos_start], nums[neg_end]
            pos_start -= 1
    
    return nums

# Test cases
assert rearrange([5, 8, -2, -2, 6, -4]) == [-4, -2, -2, 6, 8, 5]
assert rearrange([-4, -2, -2]) == [-4, -2, -2] # All negative
assert rearrange([4, 2, 2]) == [2, 2, 4] # All positive
