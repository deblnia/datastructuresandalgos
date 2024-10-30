def maxProfit(prices): 
    # here's the brute force solution 
    # profits = 0 
    # for i in range(len(prices)): 
    #     for j in range(i, len(prices)): 
    #         profits = max(profits, prices[j] - prices[i])
    # return profits if profits > 0 else 0 
    # here's a smarter one 
    # this defensive check is also good 
    if not prices: 
        return 0 
    min_price = float('inf')
    max_profit = 0
    for price in prices: 
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit 

        
# - I need to make sure I've internalized this pattern of iterating over an array in a MECE, rolling way 
#     - Basically this entails just starting from the first pointer
# - The optimization comes from the fact that you basically want the max difference. 
#     - So we take a really big number and set that as the default for min price 
#     - And we default max profit to 0 
#     - And update, update 


if __name__ == '__main__':
    assert maxProfit([7,1,5,3,6,4]) == 5 
    assert maxProfit([7,6,4,3,1]) == 0