class Node: 
	def __init__(self, val): 
		self.val = val 
		self.next = None 

def reverse_linked_list(head):
	prev = None
	curr = head 
	while curr is not None: 
		next = curr.next 
		curr.next = prev  
		# incrementing 
		prev = curr 
		curr = next 
	return prev 

# recursive version requires a different function signature!  
# slightly worse space complexity on this one? 
def reverse_linked_list_recursive(head, prev = None):
	if head is None: 
		return prev 
	next = head.next 
	head.next = prev 
	return reverse_linked_list_recursive(next, head) 
