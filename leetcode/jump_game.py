# You are given an integer array nums. You are initially positioned at the array's 
# first index, and each element in the array represents your maximum jump length at 
# that position.
# Return true if you can reach the last index, or false otherwise.

# [0, 1, 0, 0] # False
# [2, 2, 0, 0] # True
# [0, 2, 0, 0]
#  i           # max_reachable_idx = 0
#     i        # i <= max_reachable_idx, 1 > 0, max_reachable_idx = 4

# T: O(n), S: O(1), n length of list

def is_reachable(nums):
    max_reachable_idx = 0
    idx = 0

    while idx < len(nums) and idx <= max_reachable_idx:
        max_reachable_idx = max(max_reachable_idx, idx + nums[idx])
        idx += 1

    return max_reachable_idx >= len(nums) - 1

# Test cases
assert is_reachable([0, 2, 0, 0]) == False
assert is_reachable([0]) == True # One element
assert is_reachable([2,0,0]) == True # Only reachable w/ the first idx

visited = [0 for _ in range(6)]
print(visited)








