# BRUTE FORCE => 

# def min_change(amount, coins):
#   if amount == 0:
#     return 0 

#   if amount < 0:
#     return float('inf')

#   min_coins = float('inf')
#   for coin in coins: 
#     num_coins = 1 + min_change(amount - coin, coins)
#     min_coins = min(min_coins, num_coins)

#   return min_coins

# MEMOIZED => 

def min_change(amount, coins): 
  pass 

def _min_change(amount, coins, memo):
  if amount in memo: 
    return memo[amount]
  
  if amount == 0:
    return 0 

  if amount < 0:
    return float('inf')

  min_coins = float('inf')
  for coin in coins: 
    num_coins = 1 + min_change(amount - coin, coins)
    min_coins = min(min_coins, num_coins)

  return min_coins