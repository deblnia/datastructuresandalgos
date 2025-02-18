## Question I 

```python
def add_until_100(array):
    if not array: 
        return 0 

    remaining_sum = add_until_100(array[1:])

    if array[0] + remaining_sum > 100:
        return remaining_sum 

    else: 
        return array[0] + remaining_sum 
``` 

## Question II 

```python 

def golomb(n, memo={}):
    if n == 1: 
        return 1

    if n not in memo: 
        memo[n] = 1 + golomb(n - golomb(golomb(n-1, memo), memo), memo)

    return memo[n]
``` 

## Question III

Using the tuple as a dictionary key is a hack. Gotta remember that. 

```python 

def unique_paths(rows, cols, memo):
    if rows == 1 or cols == 1: 
        return 1 
    if (rows, cols) not in memo: 
        memo[(rows,cols)] = (unique_paths(rows - 1, cols, memo) + unique_paths(rows, cols - 1, memo))
    
    return memo[(rows, cols)] 
``` 
