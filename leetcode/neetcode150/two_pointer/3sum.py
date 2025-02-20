
def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    trips = []
    for i in range(len(nums) - 1):
        # skip dupe i 
        if i > 0 and nums[i] == nums[i-1]:
            continue 
        l = i + 1 
        r = len(nums) - 1
        while l < r: 
            if nums[i] + nums[l] + nums[r] == 0: 
                trips.append([nums[i], nums[l], nums[r]])
                l += 1 
                r -= 1 
                while l < r and nums[l] == nums[l -1]: 
                    l += 1 
                while l < r and nums[r] == nums[r + 1]: 
                    r -= 1 
            elif nums[i] + nums[l] + nums[r] > 0: 
                r -= 1 
            else: 
                l += 1 
    return trips 



assert threeSum([-1,0,1,2,-1,-4]) == [[-1,-1,2],[-1,0,1]]
assert threeSum([0,1,1]) == []
assert threeSum([0,0,0]) == [[0,0,0]]