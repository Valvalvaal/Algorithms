def sort_colors(colors):
    
    # My approach is going to be to create imaginary sub-arrays inside the colors
    # array, so the array of 0s comes first, then 1s then 2s.
    # To sort, I'll traverse the array from both ends toward the middle and then
    # grow each of the sub arrays at the ends. So the 0s and 2s array. At the end
    # that's going to leave the 1s in the middle
    
    # [0,1,2,2,2,0,1,2,0,0,2,1]
    #                  i
    # [0,0,0,2,0,1,1,2,1,2,2,2]
    #        l           r      start l,r pointers at the ends. check if right is 2
    
    # Traverse the entire arrary while keeping track of pointers to sub-arrays
    l, r = 0, len(colors) - 1
    i = 0
    
    while i <= r: # check nums up to the beginning of the 2s array (I know after r 
                  # all nums are organized and should be either empty or all 2s)
        # check for 0s or 2s
        if colors[i] == 0:
            # Only when I grow the 0s array I want to increment i bc I'm certain of
            # what's behind l 
            colors[i], colors[l] = colors[l], colors[i]
            l += 1
            i += 1
        elif colors[i] == 2:
            # Don't increment i bc I don't know what I moved back to colors[i] after 
            # swapping the 2 I found to colors[r]
            colors[i], colors[r] = colors[r], colors[i]
            r -= 1
        else:
            # Move past 1s bc they're going to end up where I need them by only 
            # worrying about the other two numbers
            i += 1
    
    return colors