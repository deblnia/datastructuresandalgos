import math 

class Solution: 
    def mySqrt(self, x: int) -> int:
        # I think the trick here is python's crazy default rounding  
        return math.floor(math.sqrt(x)) 