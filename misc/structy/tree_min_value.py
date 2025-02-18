from collections import deque
# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_min_value(root):
  min = float('Inf')  
  q = deque([ root ])

  while q: 
    node = q.popleft()
    if node.val < min:
      min = node.val 
    if node.left:
      q.append(node.left)
    if node.right:
      q.append(node.right)
  return min 

def tree_min_value_dfs(root): 
    if root is None:
        return float("inf")
    smallest_left_value = tree_min_value(root.left)
    smallest_right_value = tree_min_value(root.right)
    return min(root.val, smallest_left_value, smallest_right_value)