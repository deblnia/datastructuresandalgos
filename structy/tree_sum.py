from collections import deque 
class Node: 
    def __init__(self, val): 
        self.val = val 
        self.left = None 
        self.right = None 

def tree_sum_dfs(root):
    if not root: 
        return 0 
    return root.val + tree_sum_dfs(root.left) + tree_sum_dfs(root.right)

def tree_sum_bfs(root): 
    if not root:
        return 0
    q = deque([root])
    total_sum = 0 
    while q: 
        node = q.popleft()
        total_sum += node.val 

        if node.left: 
            q.append(node.left)
        if node.right: 
            q.append(node.right)
    return total_sum 
