def containsDuplicate(nums):
    return list(set(nums)) != nums 

if __name__ == '__main__': 
    assert containsDuplicate([1,2,3,1]) == True 
    assert containsDuplicate([1,2,3,4]) == False 
