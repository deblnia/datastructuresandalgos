def twoSum(nums, target):
    rv = [] 
    for i, v in enumerate(nums): 
        for j in range(i+1, len(nums)): 
            if v + nums[j] == target:
                rv.append(i)
                rv.append(j) 
    print(rv)
    return rv




if __name__ == '__main__':
    assert twoSum([2,7,11,15], 9) == [0,1]
    assert twoSum([3,2,4], 6) == [1,2]
    assert twoSum([3,3], 6) == [0,1]