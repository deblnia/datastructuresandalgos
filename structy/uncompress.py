def uncompress(s):
  i = 0 
  j = 0 
  number = '0123456789'
  rv = ''
  while j < len(s): 
    if s[j] in number: 
      j += 1
    else:
      num = int(s[i:j])
      rv += (num * s[j])
      j += 1 
      i = j
  return rv