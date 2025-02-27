def fib(n): 
    # brute force - this times out! 
    # if n == 0 or n == 1:  
    #     return n 
    # return fib(n - 1) + fib(n - 2) 
    memo = {}
    return _fib(n, memo)

def _fib(n, memo): 
    if n==0 or n==1: 
        return n 
    if n in memo:
        return memo[n]
    memo[n] = _fib(n - 1, memo) + _fib(n - 2, memo)
    return memo[n]
