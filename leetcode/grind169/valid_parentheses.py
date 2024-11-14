class Solution:
    def valid_parentheses(self, s: str): 
        p = {
            "(" : ")", 
            "[" : "]", 
            "{" : "}"
        } 
        stack = []
        for i in s:
            # opening bracket 
            if i in p:
                stack.append(i) 
            # closing bracket 
            elif i in p.values(): 
               if not stack or p[stack.pop()] != i: 
                   return False
        return len(stack) == 0 
