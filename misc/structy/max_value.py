def max_value(nums):
  mx = -float('inf')
  for i in nums: 
    mx = max(mx, i)
  return mx 

