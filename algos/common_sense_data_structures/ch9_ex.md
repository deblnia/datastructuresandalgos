## Question I 

If I were writing software for a call center that places callers on hold and
then assigns them to the next available representative, I would use a queue which
is a FIFO data structure. 

## Question II 

I would be able to read 4 from this stack. 

## Question III 

I would be able to read 3 from this queue. 

## Question IV 

I'm using the built in array as a stack instead of the previously implemented
class. 

```python
def reverse_string(str): 
   stack = [] 
   rv = ''
   for c in str: 
       stack.append(c)
    while stack: 
        rv += stack.pop()
    return rv 
``` 
