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