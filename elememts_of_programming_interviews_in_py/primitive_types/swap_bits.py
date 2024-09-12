# Flipping the values of the bits in i and j has the same effect as swapping
# them if the bits in those positions are different from each other.

def bit_sawp(x: int, j: int, i: int) -> int:
    # Check if an operation needs to be performed
    if (x >> i) & 1 != (x >> j) & 1:
        bit_mask = (1 << i) | (1 << j)
        x ^= bit_mask
    return x

test_case1 = 89    
print(bin(test_case1), bin(bit_sawp(test_case1, 1, 3)))

