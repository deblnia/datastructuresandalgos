## Question I 

The base case in this function is: 

```python 
if low > high: 
    return 
``` 

## Question II 

If we change the factorial function to calculate based on factorial(n - 2), and
change the base case to number == 1, we'll get infinite recursion depending on
the input since we would miss the base case. 

## Question III 

```python
def sum(low, high):
   if high == low: 
       return low

return high + sum(low, high - 1) 
``` 

## Question IV 

```python 
def print_all_nums(array): 
    for v in array: 
        if isinstance(v, list): 
            print_all_nums(v)
        else: print(v)
``` 
