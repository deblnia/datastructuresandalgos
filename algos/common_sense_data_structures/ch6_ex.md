## Question I. 

An algorithm that takes 3N^2 + 2N + 1 steps is said to be O(N^2) 

## Question II. 

An algorithm that takes N + log N steps has O(N) time complexity. Log N is
lower order than N so we reduce it out. 

## Question III. 

The worst case scenario for this two sum implementation is O(N^2). In this
case, we'd iterate through both arrays looking for two different numbers that
also add to 10 and we'd never find it. 

The average case scenario for two sum is some fractional constant * O(N^2),
meaning that the two numbers that sum to 10 are somewhere in the middle of the
arrays. 

The best case scenario for two sum is that the first two numbers add to 10, and
then the function terminates right away. 

## Question IV. 

The contains_x function is O(N) time, since we need to iterate through the
entire string to potentially find X. 

Optimization for best and average case: 

def contains_X(string): 
    for c in string: 
        if char == "X": 
            return True 
            break
    return False  

