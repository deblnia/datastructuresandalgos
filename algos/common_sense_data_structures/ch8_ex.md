## Question I 

```python
def intersection(array1, array2):
    d = {}
    inter = []
    for i in array1: 
        if i not in d: 
            d[i] = True  
    for i in array2: 
        if i in d: 
            inter.append(i)
    return inter 
```

## Question II 

```python
def check_duplicates(array): 
    d = {}
    for i in array: 
        if i in d: # could also use d.get() here 
            return i 
        else: d[i] = True # could also use defaultDict here 
    return None 
```
## Question III

```python
def missing_letter(string): 
    d = {}
    for c in string: 
        d[c] = True 

    a = 'abcdefghijklmnopqrstuvwxyz'

    for c in a: 
        if not d.get(c):
            return c
    return None 
```

## Question IV

```python
def non_dupe(string):
    d = {}
    for c in string: 
        if c in d: 
            d[c] += 1 
        else: d[c] = 1 
    for c in string: 
        if d[c] == 1: 
            return c 
    return None 


```
