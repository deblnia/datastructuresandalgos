from collections import Counter 
# this is kinda hacky, using built in data structures and all 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool: 
        # could use default dict? 
        if len(s) != len(t):
            return False 
        cS, cT = {}, {} 
        for i in range(len(s)): 
            cS[s[i]] = 1 + cS.get(s[i], 0) 
            cT[t[i]] = 1 + cT.get(t[i], 0)

    return cS == cT 

