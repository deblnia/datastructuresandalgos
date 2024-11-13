class Solution: 
    def two_sum(array, target): 
        d = {}
        for i, v in enumerate(array):
            if i not in d: 
                d[target - v] = i
            else: return (i, d[v]) 
