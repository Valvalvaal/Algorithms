def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    # use two pointers to compare the characters on each end of the string
    # move each towards the middle after being able to compare two alpha-num
    # characters, break if the chars on each pointer are not the same
    s = s.lower()
    l, r = 0, len(s) - 1
    match = True

    while l < r and match:
        # First case, one of the pointers points to a non alpha-num char
        if not s[l].isalnum():
            l += 1
        if not s[r].isalnum():
            r -= 1
        if s[l].isalnum() and s[r].isalnum():
            # Chars are comparable and the same
            if s[l] != s[r]:
                match = False 
            # both are alpha-num but not the same
            l += 1
            r -= 1
    return match

print(isPalindrome('catac       '))