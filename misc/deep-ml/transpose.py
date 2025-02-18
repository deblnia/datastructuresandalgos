def transpose(matrix): 
    # this is the official solution 
    # the * operator to unpack is clean 
    # return [list(i) for i in zip(*matrix)]

    # here's how I would do it first 
    rows = len(matrix)
    cols = len(matrix[0])

    t = []

    for col in range(cols): 
        new_row = []
        for row in range(rows): 
            new_row.append(matrix[row][col])
        t.append(new_row)
    return t 




assert transpose([[1,2,3],[4,5,6]]) == [[1,4],[2,5],[3,6]]