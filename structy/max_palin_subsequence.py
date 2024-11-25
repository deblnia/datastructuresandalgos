def max_palin_subsequence(string): 
    def helper(i, j): 
        # Base cases
        if i > j:
            return 0  # No characters left
        if i == j:
            return 1  # Single character is a palindrome
        
        # Recursive cases
        if string[i] == string[j]:
            return 2 + helper(i + 1, j - 1)  # Characters match
        else:
            return max(helper(i + 1, j), helper(i, j - 1))  # Exclude one end
    return helper(0, len(string) - 1)