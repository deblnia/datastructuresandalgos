def sum_possible(amount, numbers):
    # the brute force way to solve - exponential (n^a) time
    # if amount == 0:
    #     return True 
    # elif amount < 0:
    #     return False 
    # for num in numbers: 
    #     if sum_possible(amount - num, numbers):
    #         return True 
    # return False

    # here's the DP way - 
    # note that we can start with the same solution that we had for BF 
    # and just add in a memo 
    return _sum_possible(amount, numbers, {})

def _sum_possible(amount, numbers, memo):
    if amount in memo: 
        return memo[amount]
        
    if amount == 0: 
        return True 
    if amount < 0:
        return False 

    for num in numbers: 
        if _sum_possible(amount - num, numbers, memo):
            memo[amount] = True
            return True 

    memo[amount] = False 
    return False  