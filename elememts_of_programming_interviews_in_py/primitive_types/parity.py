# Keep in mind when it's necessary to do a big number of bit fiddling operations:
# Processing multiple bits at a time and caching results can improve performance

# The XOR of a group of bits is its parity, the operation is also associative. 
# the parity can be calculated by checking the XOR of half the word against the 
# other half, and repeat until we get to compare 1 bit against the other remaining bit
# T: O(logN), S: O(1)

def parity4(x: int) -> int:
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0x1


# Caching: we can compute the parity of a 64-bit int by grouping its bits into 4
# groups of 16 bits.
# T: O(n/L), S: O()

# PRECOMPUTED_PARITY = {} # Dict from 0 to 65535 as keys and values are the parities
# def parity3(x: int) -> int:
#     mask_size = 16
#     bitmask = 0xFFFF
#     # XOR will return 0 for even num of 1s or all 0s, 1 in case of odd num of 1s
#     return (
#         PRECOMPUTED_PARITY[x >> (3 * mask_size)] # gets first 16 bits of the word
#         ^ PRECOMPUTED_PARITY[x >> (2 * mask_size) & bitmask]
#         ^ PRECOMPUTED_PARITY[x >> mask_size & bitmask]
#         ^ PRECOMPUTED_PARITY[x & bitmask] # gets last 16 bits, no need to shift.
#     )



# Reduced avg time complexity by using the fact that x & (x - 1) erases the lowest  
# bit set to 1 in a bin number, so 010110 -> 010100
# T: O(k), S: O(1), k: number of 1s in word

def parity2(x: int) -> int:
    parity = 0
    while x:
        #print(bin(x), parity)
        parity ^= 1
        # parity keeps track of whether it took an even or an odd number of steps
        # to reduce x to 0 by changing all the 1s to 0s
        x &= x - 1 # drops lowest set bit of x
        # reduces x to 0 in k steps, k being the number of 1s in the bin number
    return parity


# Brute force algorithm: iterates over each bit and tracks 1s found
# T: O(N), S: O(1), N: Word size

def parity1(x: int) -> int:
    # Parity is 0 if number of 1s is even
    parity = 0
    while x:
        #  x = 001
        # When both sides of the operation are 1, means there's an even number of 1s
        # XOR operation returns 0
        parity ^= x & 1 # 1
        # parity = 1
        x >>= 1
        # x = 000
    return parity

print(parity2(7))
print(parity2(3))
print(parity2(43))
print(parity2(200))

assert parity4(7) == 1, f"expected 1, answer was {parity4(7)}"  
assert parity4(3) == 0, f"expected 0, answer was {parity4(3)}"  
assert parity4(43) == 0, f"expected 0, answer was {parity4(43)}"  
assert parity4(200) == 1, f"expected 1, answer was {parity4(200)}"  
