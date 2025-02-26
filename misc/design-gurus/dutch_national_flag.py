

def sort(arr:list[int])->list[int]:
    low, high, mid = 0, len(arr) - 1, 0  
    while mid <= high:  
        if arr[mid] == 0: 
            arr[low], arr[mid] = arr[mid], arr[low]  
            low += 1 
            mid += 1 
        elif arr[mid] == 2: 
            arr[high], arr[mid] = arr[mid], arr[high]  
            high -= 1 
        else: 
            mid += 1 
    return arr 


assert sort([1, 0, 2, 1, 0]) == [0,0,1,1,2] 
assert sort([2,2,0,1,2,0]) == [0,0,1,2,2,2]


