# Pythonic Kadane's Algorithm Implementation T: O(n), S: O(1)
def maximum_sublist2(nums):
    if not nums:
        return 0
    max_sum = curr_sum = nums[0]
    for num in nums[1:]:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)
    return max_sum

assert maximum_sublist2([3,7,-8,-1,-2,11,-2]) == 11 # len 1 sublist
assert maximum_sublist2([-1,-2,-3,-44,-2,-4,-3]) == -1 # all negatives
assert maximum_sublist2([1,2,3,3,44,5,5]) == 63 # sublist is the entire list 
assert maximum_sublist2([3, 7, -8, 11]) == 13 
assert maximum_sublist2([]) == 0

# T: O(n), S: O(1)
def maximum_sublist(nums):
    max_running_sum = float('-inf')
    running_sum = 0 

    for idx in range(len(nums)):
        # Start by adding the current num to running_sum
        running_sum += nums[idx]
        # If the current running sum is greater than the stored max sum,
        # we overwrite with the new value
        max_running_sum = max(max_running_sum, running_sum)
        # If current_sum becomes negative, drop it — start fresh
        if running_sum < 0:
            running_sum = 0
    
    return max_running_sum

assert maximum_sublist([3,7,-8,-1,-2,11,-2]) == 11 # len 1 sublist
assert maximum_sublist([-1,-2,-3,-44,-2,-4,-3]) == -1 # all negatives
assert maximum_sublist([1,2,3,3,44,5,5]) == 63 # sublist is the entire list 
assert maximum_sublist([3, 7, -8, 11]) == 13 