# def max_palin_subsequence(string): 
#     def helper(i, j): 
#         # Base cases
#         if i > j:
#             return 0  # No characters left
#         if i == j:
#             return 1  # Single character is a palindrome
        
#         # Recursive cases
#         if string[i] == string[j]:
#             return 2 + helper(i + 1, j - 1)  # Characters match
#         else:
#             return max(helper(i + 1, j), helper(i, j - 1))  # Exclude one end
#     return helper(0, len(string) - 1)

def max_palin_subsequence(string):
    return _max_palin_subsequence(string, 0, len(string) - 1, {}) 

def _max_palin_subsequence(string, i, j, memo):
    key = (i, j)
    if key in memo: 
        return memo[key]
    if i == j:
        return 1 
    if i > j: 
        return 0 
  
    if string[i] == string[j]:
      memo[key] = 2 + _max_palin_subsequence(string, i + 1, j - 1, memo)
    else: 
        memo[key] = max(
            _max_palin_subsequence(string, i + 1, j, memo), 
            _max_palin_subsequence(string, i, j - 1, memo) 
        )
    return memo[key]