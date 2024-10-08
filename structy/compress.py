def compress(s):
  s += '!'
  i = 0 
  j = 0 
  rv = ''
  while j < len(s):
    if s[i] == s[j]: 
      j += 1 
    else: 
      num = str(j-i)
      if num == '1': 
        rv += (s[i])
      else: rv += (num + s[i])
      i = j 
  return rv 


assert compress('ccaaatsss') == '2c3at3s'
assert compress('ssssbbz') == '4s2bz'
assert compress('ppoppppp') == '2po5p'