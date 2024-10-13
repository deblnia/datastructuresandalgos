class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def sum_list(head):
    # iterative -> 
    # sum = 0 
    # while head: 
    #     sum += head.val 
    #     head = head.next 
    # return sum 
    # recursive -> 
    if not head: 
       return 0 
    return head.val + sum_list(head.next)

a = Node(2)
b = Node(8)
c = Node(3)
d = Node(-1)
e = Node(7)

a.next = b
b.next = c
c.next = d
d.next = e

assert sum_list(a) == 19
