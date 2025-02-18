def makeSquares(arr):
    # # hacky built-ins, this is o(n*log(n)) time 
    # squares = sorted([x**2 for x in arr])
    # # squares.sort() # modifies in place 
    # return squares

    # what they actually want is the o(n) two pointer solution 
    n = len(arr)
    squares = [0 for _ in range(n)]

    highestSquareIdx = n - 1
    l, r = 0, n - 1

    while l <= r: 
        ls = arr[l] ** 2 
        rs = arr[r] ** 2 

        if ls >= rs: 
            squares[highestSquareIdx] = ls
            l += 1 
        else: 
            squares[highestSquareIdx] = rs 
            r -= 1
        highestSquareIdx -= 1
    return squares
        


assert makeSquares([-2, -1, 0, 2, 3]) == [0, 1, 4, 4, 9]
assert makeSquares([-3, -1, 0, 1, 2]) == [0, 1, 1, 4, 9]