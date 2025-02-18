

def searchTriplet(arr: list[int])->list[list[int]]:
    # want to find all unique triplets that sum to 0 
    arr.sort()
    trips = []
    # fix one number 
    for i, v in enumerate(arr): 
        l = i + 1 
        r = (len(arr) - 1)
        if i > 0 and arr[i] == arr[i - 1]:
            continue 
        # two pointers with the rest 
        while l < r: 
            total = v + arr[l] + arr[r] 
            if total == 0: 
                trips.append([v, arr[l], arr[r]])
                l += 1 
                r -= 1
                while l < r and arr[l] == arr[l - 1]:
                    l += 1 
                while l < r and arr[r] == arr[r + 1]:
                    r -= 1
            if total < 0: 
                l += 1 
            if total > 0: 
                r -= 1
    return trips 



assert searchTriplet([-3, 0, 1, 2, -1, 1, -2]) == [[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]]
assert searchTriplet([-5, 2, -1, -2, 3]) == [[-5, 2, 3], [-2, -1, 3]]