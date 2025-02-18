
'''
Given an integer array nums, return true if any value appears at least twice in
 the array, and return false if every element is distinct.
'''
def contains_duplicate(array: List[int]) -> bool: 
    # hacky using built in data structures 
    # return len(set(array)) < len(array)  

    # brute force 
#     for i in range(len(array)): 
#         for j in range(i + 1, len(array)): 
#             if nums[i] == nums[j]:
#                 return True 
#     return False 

    # better!
    s = set()
    for i in array: 
        if i in s: 
            return True 
        s.add(i)
    return False 
