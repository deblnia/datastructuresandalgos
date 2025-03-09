def threeSum(nums: list[int]) -> list[list[int]]:
    # res = set()
    # for i in range(len(nums) - 1): 
    #     for j in range(i + 1, len(nums)): # remember that range is exclusive on the second argument 
    #         for k in range(j + 1, len(nums)): 
    #             if nums[i] + nums[j] + nums[k] == 0: 
    #                 res.add(tuple(sorted([nums[i], nums[j], nums[k]])))
    # return sorted([list(triplet) for triplet in res])

    nums.sort()
    res = []
    for i in range(len(nums) - 2): # leaving room for the other two pointers
        # dupe check 
        if i > 0 and nums[i] == nums[i - 1]: 
            continue 
        l, r = i + 1, len(nums) - 1
        while l < r: 
            tmp_sum = nums[i] + nums[l] + nums[r]
            if  tmp_sum == 0: 
                res.append([nums[i], nums[l], nums[r]])
                r -= 1 
                l += 1 
                # skip l and r dupes 
                while l < r and nums[l] == nums[l - 1]: 
                    l += 1 
                while l < r and nums[r] == nums[r - l]: 
                    r -= 1
            elif tmp_sum < 0: 
                l += 1 
            else: 
                r -= 1 
    return res

assert threeSum([-1,0,1,2,-1,-4]) == [[-1,-1,2],[-1,0,1]]
assert threeSum([[-1,-1,2],[-1,0,1]]) == []
assert threeSum([0,0,0]) == [[0,0,0]]