from collections import defaultdict
# T: O(N), S: O(N) What if key order is not guaranteed like in newer 
# Python versions
def find_first_unique2(nums):
    freq = defaultdict(int)
    # Using an auxiliary dictionary to keep track of number frequencies
    # within the list
    
    for num in nums:
        freq[num] += 1
    
    # If order isn't guaranteed, iterate over original list
    for num in nums:
        if freq[num] == 1:
            return num

    return None

# T: O(N), S: O(N)
def find_first_unique(nums):
    frequency_dict = defaultdict(int)
    # Using an auxiliary dictionary to keep track of number frequencies
    # within the list
    
    for num in nums:
        frequency_dict[num] += 1
    
    for key, value in frequency_dict.items():
        if value == 1:
            return key

    return None