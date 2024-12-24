def makeSquares(arr):
    # hacky built-ins 
    squares = sorted([x**2 for x in arr])
    # squares.sort() # modifies in place 
    return squares





print(makeSquares([-2, -1, 0, 2, 3]))
# assert makeSquares([-2, -1, 0, 2, 3]) == [0, 1, 4, 4, 9]
# assert makeSquares([-3, -1, 0, 1, 2]) == [0, 1, 1, 4, 9]