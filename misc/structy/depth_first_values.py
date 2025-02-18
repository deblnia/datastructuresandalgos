class Node: 
    def __init__(self, val): 
        self.val = val
        self.left = None 
        self.right = None 

def depth_first_values(root):
    # iterative 
    # if root is None: 
    #     return []
    
    # values = []
    # stack = [root]
    # while stack: 
    #     curr = stack.pop()
    #     values.append(curr.val)

    #     if curr.right is not None: 
    #         stack.append(curr.right)
    #     if curr.left is not None: 
    #         stack.append(curr.left)
    # return values
    
    # recursive 
    if not root:
        return []

    left_values = depth_first_values(root.left)
    right_values = depth_first_values(root.right)

    return [root.val, *left_values, *right_values]