# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# Anagram: frequency of the characters are the same 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]] # any order is valid

# ["eat","tea","tan","ate","nat","bat"]
# "eat" - "tea" 
# sorted("eat")
# ["aet","aet","ant","aet","ant","abt"] Sort each str
# keys: "aet" values: ["eat","tea"]

# sort_strs(strs) -> new sorted_strs
# find valid anagrams by comparing the str in sorted_strs
# add valid anagrams to dict from strs
# get list of values
from collections import defaultdict

def group_anagrams(strs) -> list:
    #sorted_strs = sort_str(strs)
    anagrams_dict = defaultdict(list)

    # ["eat","tea","tan","ate","nat","bat"]
    # ["aet","aet","ant","aet","ant","abt"] 
    #  i

    # i = 0, d[sorted_strs[0]].append(d[strs[0]])

    for s in strs:
        sorted_key = "".join(sorted(s))
        anagrams_dict[sorted_key].append(s)
        # anagrams_dict = {
        # "aet": ["ate","eat","tea"],
        # "ant": ["nat","tan"],
        # "abt": ["bat"]}

    return list(anagrams_dict.values())

# def sort_str(strs):
#     return ["".join(sorted(s)) for s in strs]


print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))

assert group_anagrams([]) == []
assert group_anagrams([""]) == [[""]]