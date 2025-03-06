
def maxProduct(nums: list[int]) -> int:
    curr_prod = nums[0]
    max_prod = nums[0]

    for i in range(1, len(nums) - 1): 
        curr_prod = max(curr_prod, curr_prod * nums[i])
        if curr_prod > max_prod: 
            max_prod = curr_prod 
    return max_prod

assert maxProduct([2,3,-2,4]) == 6
assert maxProduct([-2,0,-1]) == 0 