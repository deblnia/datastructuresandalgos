
def search(nums: list[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    while l <= r: 
        mid = (l + r) // 2
        if nums[mid] == target: 
            return mid
        # find which half is sorted 
        if nums[l] <= nums[mid]: # left half is sorted 
            if nums[l] <= target < nums[mid]: # target in this half 
                r = mid - 1 
            else: 
                l = mid + 1 
        else: 
            if nums[mid] < target <= nums[r]: 
                l = mid + 1
            else:
                r = mid - 1
    return -1 



assert search(nums = [4,5,6,7,0,1,2], target = 0) == 4
assert search(nums = [4,5,6,7,0,1,2], target = 3) == -1
assert search(nums = [1], target = 0) == -1 