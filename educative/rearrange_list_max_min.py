# Rearrange a sorted list in max/min form

# Encoding the output in the input list itself
# T: O(n), S: O(1)
def rearrange_max_min3(nums):
    if not nums:
        return nums
    
    max_elem = nums[-1] + 1
    min_idx, max_idx = 0, len(nums) - 1

    for idx in range(len(nums)):
        # even idx encode
        if idx % 2 == 0:
            nums[idx] += nums[max_idx] % max_elem * max_elem
            max_idx -= 1
        else:
            nums[idx] += nums[min_idx] % max_elem * max_elem
            min_idx += 1

    return [num // max_elem for num in nums]

print(rearrange_max_min3([0,1,4]))

# Pythonic approach T: O(n), S: O(n)
def rearrange_max_min2(nums):
    result = []
    for high, low in zip(reversed(nums), nums):
        # Pairs up elements into tuples
        # [(6, 1), (5, 2), (4, 3), (3, 4), (2, 5), (1, 6)]
        result.extend([high, low])

    return result[:len(nums)] # handles odd length by

print(rearrange_max_min2([0,1,4]))

# T: O(n), S: O(n)
def rearrange_max_min(nums):
    result = []
    low, high = 0, len(nums) - 1

    while low <= high:
        if low != high:
            result.append(nums[high])
            result.append(nums[low])
        else: 
            result.append(nums[high])
        high -= 1
        low += 1

    return result

# Test cases
assert rearrange_max_min([]) == []
assert rearrange_max_min([0]) == [0]
assert rearrange_max_min([0,1,4]) == [4,0,1]

