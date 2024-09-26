def maxProfit(prices): 
    # here's the brute force solution 
    # profits = 0 
    # for i in range(len(prices)): 
    #     for j in range(i, len(prices)): 
    #         profits = max(profits, prices[j] - prices[i])
    # return profits if profits > 0 else 0 
    # here's a smarter one 
    if not prices: 
        return 0 
    min_price = float('inf')
    max_profit = 0
    for price in prices: 
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit 

        







if __name__ == '__main__':
    assert maxProfit([7,1,5,3,6,4]) == 5 
    assert maxProfit([7,6,4,3,1]) == 0