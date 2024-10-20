## Question I. 

| N Elements | O(N)  |O(logN)| O(N^2) |
| --- | --- | --- | --- |
| 100  | 100 | 2^x = 100, x = 6.6 | 10,000 |
| 2000 | 2000 | 10.9  | 4,000,000 |
	


## Question II. 

If O(N^2) takes 256 steps, there must be sqrt(256) = 16  elements in the array. 

## Question III.

This function to find the greatest product of any pair of two numbers within a
given array runs in O(N^2) time where N is the size of the array. 

## Question IV. 

def greatest_number(array):
	if not array:
		return None 
	curr_greatest = -float("Inf")
	for i in array:
		if i > curr_greatest:
			curr_greatest = i
	return curr_greatest if curr_greatest != -float("Inf") else None 
