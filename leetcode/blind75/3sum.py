def threeSum(nums: list[int]) -> list[list[int]]:
    res = set()
    for i in range(len(nums) - 1): 
        for j in range(i + 1, len(nums)): 
            for k in range(j + 1, len(nums)): 
                if nums[i] + nums[j] + nums[k] == 0: 
                    res.add(tuple(sorted([nums[i], nums[j], nums[k]])))
    print(sorted([list(triplet) for triplet in res]))
    return sorted([list(triplet) for triplet in res])

assert threeSum([-1,0,1,2,-1,-4]) == [[-1,-1,2],[-1,0,1]]
assert threeSum([[-1,-1,2],[-1,0,1]]) == []
assert threeSum([0,0,0]) == [[0,0,0]]