def maxProfit(prices: list[int]) -> int:
    max_profit = 0
    min_price = prices[0]
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit


assert maxProfit([7, 1, 5, 3, 6, 4]) == 5
assert maxProfit([7, 6, 4, 3, 1]) == 0


def maxProfit(prices: list[int]) -> int:
    mx = 0
    min_price_so_far = float("Inf")

    for i, v in enumerate(prices):
        if v - min_price_so_far > mx:
            mx = v - min_price_so_far
        if v < min_price_so_far:
            min_price_so_far = v
    return mx


# could also use two pointer e.g.
def maxProfit(prices: list[int]) -> int:
    l, r = 0, 1  # Left is the buy day, right is the potential sell day
    mx = 0

    while r < len(prices):
        if prices[r] > prices[l]:
            mx = max(mx, prices[r] - prices[l])  # Update max profit
        else:
            l = r  # Move buy day forward if we find a lower price
        r += 1  # Always move sell day forward

    return mx


assert maxProfit([10, 1, 5, 6, 7, 1]) == 6
assert maxProfit([10, 8, 7, 5, 2]) == 0
