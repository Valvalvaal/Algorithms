# Find two numbers that add up to k

def binary_search(lst, elem):

    l = 0
    h = len(lst) - 1

    found = False
    idx = -1

    while l < h and not found:
        mid = (l + h) // 2

        if lst[mid] == elem:
            idx = mid
            found = True
        else:
            if lst[mid] < elem:
                l = mid + 1
            else:
                h = mid - 1
    
    if found:
        return idx
    else:
        return -1



def find_pair(nums, k):
    # One approach to solve is to have binary search find the complement of
    # each number of the list so that it adds up to k
    # k = number at idx + complement, complement = number at idx - k

    # Sort the list so that binary search can be applied
    nums.sort() # runs in O(nlogn)

    for curr_idx in range(len(nums)):
        idx_of_complement = binary_search(nums, k - nums[curr_idx])

        # If binary search found an index for a possible complement to the 
        # number at curent_idx and that index isn't itself, then we found
        # the missng indx to form the valid pair
        if idx_of_complement != -1 and idx_of_complement != curr_idx:
            return [nums[curr_idx], nums[idx_of_complement]]
        

print(find_pair([1,10,8,4,9], 17))
print(find_pair([-10,-8,-7,-4,-3,0], -15))