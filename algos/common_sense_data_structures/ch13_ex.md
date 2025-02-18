## Question I 

```python 
def greatest_product(array): 
    if len(array) < 3: 
        return -1 
    array = array.sort()
    return array[-1] * array[-2] * array[-3] 
```


## Question II 

```
def find_missing_number(array):
    array.sort()

    for i, v in enumerate(array):
        if v != i: 
            return i
    return None 
```

## Question III 

O(N^2) implementation can have nested loops. 

```python 
def max(array): 
    if not array:
        return None 
    for i in array: 
        i_greatest = True 
        for j in array: 
            if j > i: 
                i_greatest = False 
        if i_greatest:
            return i 
```
The O(NlogN) sorts the array and returns the last number. 

```python 

def max(array): 
    if not array: 
        return None 
    array.sort()
    return array[-1] 

```

The O(N) solution can only have one loop. 

```python 
def max(array): 
    if not array: 
        return None 

    greatest_num_so_far = array[0] 

    for num in array: 
        if num > greatest_num_so_far: 
            greatest_num_so_far = num 
    return greatest_num_so_far 

``` 
