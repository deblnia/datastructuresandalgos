import math 
# BRUTE FORCE - TIMESOUT 
# def summing_squares(n):
#   if n == 0:
#     return 0

#   min_squares = float('inf')
#   for i in range(1, math.floor(math.sqrt(n)) + 1):
#     square = i * i 
#     num_squares = 1 + summing_squares(n - square)  
#     min_squares = min(min_squares, num_squares)
#   return min_squares