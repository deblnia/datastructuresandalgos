class Solution:
    def valid_parentheses(self, string:str): -> bool 
        p = {"(" : ")", 
            "{" : "}", 
            "[" : "]"
        }
        stack = []
        for c in string: 
            if c in p: 
                stack.append(c)
            elif c in p.values(): 
                if not stack and stack.pop() != p[c]:
                    return False 
            return len(stack) == 0 
