class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def linked_list_find(head, target): 
    # iterative
    # while head: 
    #     if head.val == target:
    #       return True 
    #     head = head.next 
    # return False  
    # recursive 
    if not head: 
       return False 
    if head.val == target:
       return True 
    return linked_list_find(head.next, target)




a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

assert linked_list_find(a, "c") == True 