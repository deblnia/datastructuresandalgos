def matrix_dot_vector(a:list[list[int|float]],b:list[int|float])-> list[int|float]:
	""""
	Example:
        input: a = [[1,2],[2,4]], b = [1,2]
        output:[5, 10] 
        reasoning: 1*1 + 2*2 = 5;
                   1*2+ 2*4 = 10
	http://matrixmultiplication.xyz/
	"""
	if len(b) != len(a[0]):
		return -1 
	vals = []
	# iterating through the first row 
	for i in a: 
		hold = 0 
		# iterating through the 
		for j in range(len(i)): 
			hold += (i[j] * b[j])
		vals.append(hold)
	return vals 

assert matrix_dot_vector([[1,2,3],[2,4,5],[6,8,9]],[1,2,3]) == [14, 25, 49]