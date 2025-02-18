def most_frequent_char(s):
  d = {}
  for c in s: 
    if c not in d: 
      # this could maybe be a default dict? 
      d[c] = 1 
    else: d[c] += 1 

  most_freq = ''
  max_count = 0
  for i in s: 
    if d[i] > max_count: 
      most_freq = i
      max_count = d[i]
  return most_freq

assert most_frequent_char('bookeeper') == 'e'
assert most_frequent_char('david') == 'd'