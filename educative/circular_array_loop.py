def circular_array_loop(nums):  
    arr_len = len(arr)
    visited = {}
    idx = 0
    
    while arr_len:
        idx += nums[idx]
        if idx in visited:
            return True
        idx = idx if (idx < len(nums)) and (idx > 0) else idx - len(nums) 
        visited.add(idx)
        arr_len -= 1

    return False