from collections import deque 
# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def max_path_sum(root):
  if not root: 
    return float("-inf")
  # checking for leaf node 
  if not root.left and not root.right:
    return root.val 
  return root.val + max(max_path_sum(root.left), max_path_sum(root.right))


def max_path_sum_bfs(root): 
    if not root:
        return float("-inf")

    max_sum = float("-inf")
    queue = deque([(root, root.val)])  # Each entry is a tuple (node, cumulative_sum)

    while queue:
        node, current_sum = queue.popleft()

        # Check if it's a leaf node
        if not node.left and not node.right:
            max_sum = max(max_sum, current_sum)
        
        # Add children to queue with updated path sums
        if node.left:
            queue.append((node.left, current_sum + node.left.val))
        if node.right:
            queue.append((node.right, current_sum + node.right.val))

    return max_sum