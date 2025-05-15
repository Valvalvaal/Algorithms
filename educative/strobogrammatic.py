def is_strobogrammatic(num: str):
    # Solution: Initiate two pionters check every number against its corresponding position
    # after the flip, if the numbers are each other's strobogrammatic complements, move inward, 
    # repeat

    # 1001
    # l  r -> num[l]->1 is strobogrammatic complement of num[r]->1, true
    #  lr  -> 0 is strobogrammatic complement of 0, true
    # True

    # 121
    # l r -> 1 is strobogrammatic complement of 1, true
    #  l  -> 2 is not strobogrammatic, false

    l, r = 0, len(num) - 1 # Could be useful for other problems: Only 1 pointer works bc they move symmetrically

    # Check each num against its corresponding position after the flip
    while l <= r:
        if not is_strobogrammatic_complement(num[l],num[r]):
            return False
        l += 1
        r -= 1

    return True

def is_strobogrammatic_complement(num1,num2):
    # Dict with all strob nums
    strobogrammatic = {
        "0":"0",
        "1":"1",
        "6":"9",
        "9":"6",
        "8":"8"
    }
    if not (num1 in strobogrammatic.keys()):
        return False

    return strobogrammatic[num1] == num2


# Test Case 1: "121"
assert not is_strobogrammatic("121"), f"""Expected False, actual: {is_strobogrammatic("121")}"""

# Test Case 2: "1881"
assert is_strobogrammatic("1881"), f"""Expected True, actual: {is_strobogrammatic("1881")}"""

# Test Case 3: "1"
assert is_strobogrammatic("1"), f"""Expected False, actual: {is_strobogrammatic("1")}"""

# Test Case 4: "696"
assert not is_strobogrammatic("696"), f"""Expected False, actual: {is_strobogrammatic("696")}"""

# Test Case 5: ""
assert is_strobogrammatic(""), f"""Expected False, actual: {is_strobogrammatic("")}"""
