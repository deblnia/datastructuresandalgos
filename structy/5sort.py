def five_sort(nums):
#   l = 0
#   r = len(nums) - 1 
#   while l <= r: 
#     if nums[r] == 5: 
#       r -= 1 
#     elif nums[l] == 5: 
#       # nice python syntax, can also use a tmp variable 
#       nums[l], nums[r] = nums[r], nums[l]
#       l += 1 
#     else: l += 1 
#   return nums 
    l = 0 
    r = len(nums) - 1
    while l <= r: 
        if nums[r] == 5: 
            r -= 1
        elif nums[l] == 5: 
            tmp_r = nums[r]
            nums[r] = 5 
            nums[l] = tmp_r 
            l += 1 # could do either the decrement or the increase here   
        else: l += 1
    return nums 

assert five_sort([12, 5, 1, 5, 12, 7]) == [12, 7, 1, 12, 5, 5] 
assert five_sort([5, 2, 5, 6, 5, 1, 10, 2, 5, 5]) == [2, 2, 10, 6, 1, 5, 5, 5, 5, 5] 
assert five_sort([5, 5, 5, 1, 1, 1, 4]) == [4, 1, 1, 1, 5, 5, 5] 
assert five_sort([5, 5, 6, 5, 5, 5, 5]) == [6, 5, 5, 5, 5, 5, 5] 
assert five_sort([5, 1, 2, 5, 5, 3, 2, 5, 1, 5, 5, 5, 4, 5]) == [4, 1, 2, 1, 2, 3, 5, 5, 5, 5, 5, 5, 5, 5] 