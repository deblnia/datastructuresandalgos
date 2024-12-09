import math 

class Solution: 
    def mySqrt(self, x: int) -> int:
        # I think the trick here is python's crazy default rounding  
        # return math.floor(math.sqrt(x)) 
        # okay no they actually wanted to do it 
        if x < 2: 
            return x # 0 or 1 case 
        
        l, r = 2, x // 2 
        mid = 0 
        num = 0 
        while l <= r: 
            mid = l + (r - l) # middle element 
            num = mid * mid 
            if num > x: 
                r = mid - 1 
            elif num < x: 
                l = mid + 1 
            else: 
                return mid 
        return r 
