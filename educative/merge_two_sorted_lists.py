# T:O(n+m) because of list concatenation, S: O(n+m)
def merge_lists(nums1, nums2):
    # Traverse both lists starting idx 0, compare elements and add the smallest
    # item between the two lists to the array, move the pointer as we add elems
    # to the return list
    i, j = 0, 0
    merged_list = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            merged_list.append(nums1[i])
            i += 1
        else:
            merged_list.append(nums2[j])
            j += 1
    return merged_list + nums2[j:] if i >= len(nums1) else merged_list + nums1[i:]