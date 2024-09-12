# Function to count bits set to 1 in a bin number

def count_bits(n: int) -> int:
    # n = 7, bin(n) -> 111
    num_bits = 0
    while n:
        print(bin(n), num_bits)
        num_bits += n & 1 # 1
        # 1
        n >>= 1
        # n = 011
    return num_bits

print(count_bits(7))