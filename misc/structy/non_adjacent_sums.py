def non_adjacent_sum(nums):
    # this is the brute force way 
    if len(nums) == 0: 
        return 0 

    include = nums[0] + non_adjacent_sum(nums[2:])
    exclude = non_adjacent_sum(nums[1])

    return max(include, exclude)

# abstracting away the slicing gets some efficiency gains 
# since you have to make fewer copies of the array 
def non_adjacent_sum(nums):
  return _non_adjacent_sum(nums, 0, {})



def _non_adjacent_sum(nums, i, memo):
  if i in memo: 
    return memo[i]
    
  if i >= len(nums):
    return 0

  include = nums[i] + _non_adjacent_sum(nums, i + 2, memo)
  exclude = _non_adjacent_sum(nums, i + 1, memo)
  memo[i] = max(include, exclude)

  return max(include, exclude)

