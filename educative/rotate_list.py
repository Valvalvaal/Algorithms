# Slicing solution T: O(n), S:O(n)
def rotate_list3(nums, k):
    length = len(nums)
    k %= length

    if k == 0:
        return nums[:]
    
    reversed_list = nums[-k:] + nums[:-k]
    return reversed_list

# Test cases
assert rotate_list3([10, 20, 30, 40, 50], 8) == [30, 40, 50, 10, 20]
assert rotate_list3([10], 8) == [10]


# Optimized solution T: O(n), S: O(1)
def rotate_list2(nums, k):
    n = len(nums)
    k %= n

    reverse(nums, 0, n - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, n - 1)

    return nums

def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1


# Test cases
assert rotate_list2([10, 20, 30, 40, 50], 8) == [30, 40, 50, 10, 20]
assert rotate_list2([10], 8) == [10]


# T: O(n), S: O(n)

# Idea: k can be very big, but in the end, the real shift is only 
# going to be of at most n-1 steps. n steps means the list ends up 
# the same.
# To simplify k, k % len(nums) -> will give us the real number of 
# steps to shift all positions
# Then, my idea to do the shift is to calculate the final positions 
# of the numbers in the list and re-positioning the elems and assigning
# the numbers to those positions
# [10, 20, 30, 40, 50], k = 8 -> k % len(nums) -> 8 % 5 = 3
#  i                  , i = 0 -> i + 3 = 3, new[3], new = [x, x, x, 10, x]
#      i              , i = 1 -> i + 3 = 4, new[4], new = [x, x, x, 10, 20]
#           i         , i = 2 -> i + 3 = 5, new[5%len] -> new[0], new = [30, x, x, 10, 20]
#               i     , i = 3 -> i + 3 = 6, new[6%len] -> new[1], new = [30, 40, x, 10, 20]
#                  i  , i = 4 -> i + 4 = 7, new[7%len] -> new[2], new = [30, 40, 50, 10, 20]

def rotate_list(nums, k):
    n = len(nums)
    k %= n

    if k == 0:
        return nums[:]

    result = [0] * n
    for idx in range(n):
        new_idx = (idx + k) % n
        result[new_idx] = nums[idx]
    
    return result

# Test cases
assert rotate_list([10, 20, 30, 40, 50], 8) == [30, 40, 50, 10, 20]
assert rotate_list([10], 8) == [10]