def non_adjacent_sum(nums):
    # this is the brute force way 
    if len(nums) == 0: 
        return 0 

    include = nums[0] + non_adjacent_sum(nums[2:])
    exclude = non_adjacent_sum(nums[1])

    return max(include, exclude) 
