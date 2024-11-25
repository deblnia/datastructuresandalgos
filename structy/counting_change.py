def counting_change(amount, coins): 
    def helper(remaining, index): 
        if remaining == 0:
            return 1 
        if remaining < 0 or index == len(coins): 
            return 0
        
        # include current coin or skip 
        inc = helper(remaining - coins[index], index)
        exc = helper(remaining, index + 1)
        return inc + exc
    return helper(amount, 0)