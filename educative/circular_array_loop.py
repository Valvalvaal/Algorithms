def circular_array_loop(nums):  
    arr_len = len(nums)
    visited = {0}
    idx = 0
    
    while arr_len:
        print(idx)
        idx += nums[idx]
        if idx in visited:
            return True
        idx = idx if (idx < len(nums)) and (idx > 0) else idx - len(nums) 
        visited.add(idx)
        arr_len -= 1

    return False

# Two Pointer Solution
def circular_array_loop(nums):
    size = len(nums)
    
    for i in range(size):
        slow = fast = i
        forward = nums[i] > 0
      
        while True:
            slow = next_step(slow, nums[slow], size) 
            if is_not_cycle(nums, forward, slow):
                break
        
            fast = next_step(fast, nums[fast], size)
            if is_not_cycle(nums, forward, fast):
                break
            
            fast = next_step(fast, nums[fast], size)
            if is_not_cycle(nums, forward, fast):
                break
        
            if slow == fast:
                return True
                
    return False

# A function to calculate the next step
def next_step(pointer, value, size):
    return (pointer + value) % size


# A function to detect a cycle doesn't exist
def is_not_cycle(nums, prev_direction, pointer):
    curr_direction = nums[pointer] >= 0
    
    if (prev_direction != curr_direction) or (nums[pointer] % len(nums) == 0):
        return True
    else:
        return False