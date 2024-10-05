def twoSum(nums, target):
    # this is the brute force 
    # rv = [] 
    # for i, v in enumerate(nums): 
    #     for j, k in enumerate(nums[1:]): 
    #         print(v, k)
    #         if v + k == target:
    #             rv.append(i)
    #             rv.append(j+1) 
    #             print(f'RV --> {rv}')
    #             return rv
    # this is the smart one pass solution
    # it stores the difference as the key 
    # and the index as a the value  
    d = {} 
    for i, num in enumerate(nums): 
        if num in d: 
            return [d[num], i]
        else: 
            d[target - num] = i




if __name__ == '__main__':
    assert twoSum([2,7,11,15], 9) == [0,1]
    assert twoSum([3,2,4], 6) == [1,2]
    assert twoSum([3,3], 6) == [0,1]