def min_moves_to_make_palindrome(s):
    # Idea: Using two pointers, traverse the string from the front and 
    # back simultaneously while checking whether the left_char is the same as
    # the right char. 
    # If the chars are not the same, then using an inner loop, find the match for 
    # the number in the left and swap accordingly to place in the right position.

    # 0123456
    # arcacer -> racecar
    # l     r -> a == r -> False, search for a match with inner loop
    #  l   r  -> r found in position 1, if matches s[r], count moves to shift to l
    # racacer 
    #  l   r  -> a == e -> False, search for a match with inner loop
    #   l r

    
    l, r = 0, len(s) - 1

    while l < r:


        l += 1
        r -= 1

    return 0