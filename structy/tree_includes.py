from collections import deque 
# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_includes(root, target):
  if not root:
    return False 
  q = deque([root]) 
  while q: 
    node = q.popleft()
    if node.val == target:
      return True
    if node.left: 
      q.append(node.left)
    if node.right:
      q.append(node.right)
  return False 

def tree_includes_dfs(root, target):
  if not root:
    return False
  
  if root.val == target:
    return True
  
  return tree_includes(root.left, target) or tree_includes(root.right, target)