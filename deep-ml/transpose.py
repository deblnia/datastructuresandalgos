def transpose(matrix): 
    # this is the official solution 
    # the * operator to unpack is clean 
    # return [list(i) for i in zip(*matrix)]

    # here's how I would do it first 



assert transpose([[1,2,3],[4,5,6]]) == [[1,4],[2,5],[3,6]]