class Solution:
    def two_sum(self, target, array[List[int]]): -> (int, int):
        d = {}
        for i, v in enumerate(array):
            if v not in d:
                d[target - v] = i
            else: 
                return (d[v], i) 
