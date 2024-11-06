def tribonacci(n):
    # this is the brute force / timeout version 
    # if n == 0 or n == 1:
    #     return 0 
    # if n == 2: 
    #     return 1 
    # return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)
    memo = {}
    return _trib(n, memo)

def _trib(n, memo): 
  if n == 0 or n == 1: 
    return 0
  if n == 2: 
    return 1 
  if n in memo:
    return memo[n]
  memo[n] = _trib(n - 1, memo) + _trib(n - 2, memo) + _trib(n - 3, memo)
  return memo[n]