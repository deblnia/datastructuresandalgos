
def maxSubArray(nums: list[int]) -> int:
    # finding subarray with max sum 
    # sliding window NO kadane's 
    # use kadane's when no constraints 
    curr_sum = nums[0] # best subarray that ends at index i 
    max_sum = nums[0] # should I extend or start a new array

    for i in range(1, len(nums)):
        curr_sum = max(nums[i], curr_sum + nums[i]) 
        if curr_sum > max_sum: 
            max_sum = curr_sum 
    return max_sum


assert maxSubArray([1]) == 1 
assert maxSubArray([5,4,-1,7,8]) == 23 


