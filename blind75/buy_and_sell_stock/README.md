# buy and sell stock 

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

----- 
- I need to make sure I've internalized this pattern of iterating over an array in a MECE, rolling way 
    - Basically this entails just starting from the first pointer
- The optimization comes from the fact that you basically want the max difference, so you need to find the max max and the min min 
