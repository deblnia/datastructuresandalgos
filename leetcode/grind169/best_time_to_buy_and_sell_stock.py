

def maxProfit(prices: list[int]) -> int:
    mx = 0 
    min_price_so_far = float('Inf')
    
    for i, v in enumerate(prices): 
        if v - min_price_so_far > mx: 
            mx = (v - min_price_so_far)
        if v < min_price_so_far: 
            min_price_so_far = v  
    return mx 


assert maxProfit([10,1,5,6,7,1]) == 6 
assert maxProfit([10,8,7,5,2]) == 0 