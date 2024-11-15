class Solution: 
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for i in strs: 
            srt = ''.join(sorted(i))
            if srt in ans:
                ans[srt].append(i) 
            else: ans[srt] = [i]
        return list(ans.values())

# could also use a default dict 
from collection import defaultdict 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: 
        ans = defaultdict(list) 
        for i in strs:
            srt = ''.join(sorted(i))
            ans[srt].append(i) 
        return list(ans.values())
