
```python 

class Node: 
    def __init__(self, data):
        self.data = data 
        self.next_node = None 

class LinkedList: 
    def __init__(self, first_node=None):
        self.first_node = first_node 

    def read(self, index):
        current = self.first_node 
        curr_index = 0 

        while curr_index < index: 
            current = current.next_node 
            current_index += 1 

            if not current: 
                return None
        return current.data

    def search(self, value):
        current = self.first_node 
        curr_index = 0 

        while True: 
            if current.data == value: 
                return curr_index 
            current = current.next_node 
            if not current: 
                break 
            current_index += 1 
        return None 

    def insert(self, index, value): 
        new = node.Node(value) 
        if index == 0: 
            new_node.next_node = self.first_node 
            self.first_node = new_node 
            return 
        
        current = self.first_node 
        current_index = 0 
        while current_index < (index - 1): 
            current_node = current_node.next_node 
            current_index += 1 

        new_node.next_node = current_node.next_node 
        current_node.next_node = new_node 

    def delete(self, index): 
        if index == 0:
            self.first_node = self.first_node.next_node 
            return 

        current_node = self.first_node 
        current_index = 0 

        while current_index < (index - 1): 
            current_node = current_node.next_node 
            current_index += 1 

            node_after_deleted_node = current_node.next_node.next_node 
            current_node.next_node = node_after_deleted_node 

```
```python 

class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next_node = None 
        self.previous_node = None 

class DoublyLinkedList: 
    def __init__(self, first_node=None, last_node=None): 
        self.first_node = first_node 
        self.last_node = last_node 

    def append(self, value): 
        new_node = node.Node(value) 

        if not self.first_node:
            self.first_node = new_node 
            self.last_node = new_node 
        else: 
            new_node.previous_node = self.last_node 
            self.last_node.next_node = new_node 
            self.last_node = new_node 
    
    def pop_head(self):
        popped_node = self.first_node 
        self.first_node = self.first_node.next_node 
        self.first_node.previous_node = None 
        return popped_node 

class Queue: 
    def __init__(self): 
        self.data = DoublyLinkedList() 

    def enqueue(self, element):
        self.data.append(element) 

    def dequeue(self):
        dequeued_node = self.data.pop_head() 
        return dequeued_node.data 

    def read(self):
        if not self.data.first_node: 
            return None 
        return self.data.first_node.data 


```

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
