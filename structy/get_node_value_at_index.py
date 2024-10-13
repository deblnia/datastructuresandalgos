class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def get_node_value(head, index):
    # iterative way 
    # for _ in range(index):
    #     if not head: 
    #        return None  
    #     head = head.next
    # return head.val 

    # recursive way 
    if not head:
       return None
    if index == 0: 
       return head.val 
    return get_node_value(head.next, index - 1)






a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

assert get_node_value(a, 7) == None 


node1 = Node("banana")
node2 = Node("mango")

node1.next = node2

# banana -> mango

assert get_node_value(node1, 0) == 'banana'