def pair_sum(numbers, target_sum):
  d = {}
  for i,v in enumerate(numbers):
    if v not in d: 
      d[target_sum - v] = i 
    else: 
      return (d[v], i)
    
assert pair_sum([3, 2, 5, 4, 1], 8)  == (0, 2)
assert pair_sum([4, 7, 9, 2, 5, 1], 5) == (0,5)