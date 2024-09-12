print(bin(9223372036854775807))
print(len('1111111111111111'))

# T: O(N/L), S: O(N/L), L: length of mask_size

PRECOMPUTED_REVERSE = {}

def reverse_bits(x: int) -> int:
    mask_size = 16
    bit_mask = 0xFFFF
    return (
        PRECOMPUTED_REVERSE[x & bit_mask] << (3 * mask_size) # get 16 LSBs from x, shift them to the 16 MSB places
        | PRECOMPUTED_REVERSE[x >> mask_size & bit_mask] << (2 * mask_size) # "Paste" those bits using OR operation
        | PRECOMPUTED_REVERSE[x >> (mask_size * 2) & bit_mask] << mask_size
        | PRECOMPUTED_REVERSE[x >> (mask_size * 3) & bit_mask]
    )