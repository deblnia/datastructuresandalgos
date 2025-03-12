
def findMin(nums: list[int]) -> int:
    # pretty inefficient two pointer approach -> 
    # l, r = 0, len(nums) - 1
    # curr_min = nums[l] 
    # while l < r: 
    #     if nums[l] < nums[r]:
    #         curr_min = min(nums[l], curr_min)
    #         r -= 1 
    #     elif nums[l] > nums[r]:
    #         curr_min = min(nums[r], curr_min)
    #         l += 1 
    #     else: 
    #         l += 1 
    # return curr_min
    # better binary search approach -> 
    l, r = 0, len(nums) - 1 
    while l < r: 
        mid = (l + r) // 2 
        if nums[mid] > nums[r]: # min must be in the right half 
            l = mid + 1 
        else: 
            r = mid 
    return nums[l]


assert findMin([3,4,5,1,2]) == 1 
assert findMin([4,5,6,7,0,1,2]) == 0
assert findMin([11,13,15,17]) == 11 
assert findMin([2,1]) == 1
assert findMin([3, 1, 2]) == 1 
