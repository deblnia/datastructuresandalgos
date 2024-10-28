from collections import deque  

def class Node: 
	def __init__(self, val): 
                self.val = val 
                self.left = None 
                self.right = None 


def breadth_first_values(root):
        q = deque([root]) 
        values = [] 

        while q: 
                node = q.popleft()
                values.append(node.val)

                if node.left: 
                        q.append(node.left)
                if node.right:
                        q.append(node.right) 
       return values 
