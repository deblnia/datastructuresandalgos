def search(arr, target): 
    d = {}
    for i, v in enumerate(arr):
        if v in d:
            return [d[v], i]
        else: 
            d[target-v] = i
    return [-1,-1]
