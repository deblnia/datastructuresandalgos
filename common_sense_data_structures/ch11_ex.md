## Question I 

```python 

def total_characters(arr): 
    if not arr: 
        return 0 
    return len(arr.pop()) + total_characters(arr) 
# if the array needs to be returned, could use 
# return len(array[0]) + total_characters(array[1:]) 
```

## Question II 

```python 

def just_even(array):
    if not array:
        return []
    if array[0] % 2 == 0: 
        return [array[0]] + just_even(array[1:])
    else: 
        return just_even(array[1:])

```

## Question III 

```python
def triangular(n): 
    if n == 1: 
        return 1 
    return n + triangular(n-1) 


```

## Question IV 

```python 

def find_x(str, x):
    if str[0] == x: 
        return 0 
    return find_x(str[1:], x) + 1 

```

## Question V 

```python 

def unique_paths(rows, cols): 
    if rows == 1 or cols == 1: 
        return 1 
    return unique_paths(rows - 1, cols) + unique_paths(rows, cols - 1) 
``` 
