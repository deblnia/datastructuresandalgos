

def searchTriplet(arr:list[int], target_sum:int)->int:
    # want to find triplet in the array who's sum is as close to target
    arr.sort()
    min_dist = float('inf')
    best_total = 0

    for i,v in enumerate(arr): 
        left = i + 1 
        right = len(arr) - 1
        while left < right: 
            total = v + arr[left] + arr[right]
            curr_dist = abs(target_sum - total)

            if curr_dist < min_dist:
                min_dist = curr_dist
                best_total = total 
            
            if total < target_sum:
                left += 1 
            elif total > target_sum: 
                right -= 1 
            else: 
                return total
    return best_total 

assert searchTriplet([-1, 0, 2, 3], 3) == 2
assert searchTriplet([-3, -1, 1, 2], 1) == 0 
assert searchTriplet([1, 0, 1, 1], 100) == 3 
