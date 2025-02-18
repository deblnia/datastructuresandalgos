# Brute Force 
# def can_concat(s, words):
#   if s == '': 
#     return True 
#   for word in words: 
#     if s.startswith(word):
#       suffix = s[len(word):] 
#       if can_concat(suffix, words) == True:
#         return True
#   return False 


def can_concat(s, words):
  return _can_concat(s, words, {})

def _can_concat(s, words, memo):
  if s in memo:
    return memo[s]
    
  if s == '': 
    return True 
  for word in words: 
    if s.startswith(word):
      suffix = s[len(word):] 
      if _can_concat(suffix, words) == True:
        memo[s] = True 
        return True
  memo[s] = False 
  return False 