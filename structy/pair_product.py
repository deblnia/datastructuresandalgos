def pair_product(numbers, target_product):
  d = {}
  for i,v in enumerate(numbers):
    if v not in d:
      d[target_product / v] = i 
    else: return (d[v], i)


assert pair_product([3, 2, 5, 4, 1], 8) == (1,3)