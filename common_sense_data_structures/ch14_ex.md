## Question I 

```python 
def print_list(self):
    curr = self.first_node 
    while curr: 
        print(curr.val) 
        curr = curr.next_node 
```
## Question II 

```python 
class DoublyLinkedList: 
    def __init__(self, first_node=None, last_node=None):
        self.first_node = first_node 
        self.last_node = last_node 
    def print_reverse(self): 
        curr = self.last_node 
        while curr: 
            print(curr.val) 
            curr = curr.previous_node 
```
## Question III 

Using the next_node as a while condition is more elegant here. My initial
attempt used the usual iteration with a conditional which felt cumbersome. 

```python 
def last_value(self):
    curr = self.first_node 
    while curr.next_node: 
        curr = curr.next_node 
    return curr.data 
``` 

## Question IV 

I always forget this. Trying to think in terms of anchor, pivot, and scout. 

```python 

def reverse_linked_list(self):
    curr = self.first_node 
    prev = None 
    while curr: 
        nxt = curr.next_node 
        curr.next = prev 
        prev = curr 
        curr = nxt  
    return prev
``` 

The solution in the book also sets the `self.first_node = previous_node` but
I'm using the Linked List definition I'm used to. 

## Question V

```python 
def delete_node(node): 
    node.data = node.next_node.data 
    node.next_node = node.next_node.next_node 
``` 
