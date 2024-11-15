def containsDuplicate(nums: List[int]) -> bool:
    return len(set(nums)) != len(nums)
# this is probably a hacky solution since it's using built-in data structures 

def containsDuplicate(nums):
    d = {}
    for num in nums: 
        if num not in d:
            d[num] = 0 
        else: return True 
    return False 
