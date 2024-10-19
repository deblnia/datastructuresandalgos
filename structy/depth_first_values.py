class Node: 
    def __init__(self, val): 
        self.val = val
        self.left = None 
        self.right = None 

def depth_first_values(root):
    if root is None: 
        return []
    
    values = []
    stack = [root]
    while stack: 
        curr = stack.pop()
        values.append(curr.val)

        if curr.right is not None: 
            stack.append(curr.right)
        if curr.left is not None: 
            stack.append(curr.left)
    return values 