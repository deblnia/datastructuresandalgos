

def searchTriplet(arr:list[int], target_sum:int)->int:
    # want to find triplet in the array who's sum is as close to target
    arr.sort()
    min_dist = float('inf')

    for i in range(len(arr) - 2): 
        left = i + 1 
        right = len(arr) - 1
        while left < right: 
            target_diff = target_sum - (arr[i] + arr[left] + arr[right])
            
            if target_diff == 0: 
                return target_sum
            
            if abs(target_diff) < abs(min_dist) or (abs(target_diff) == abs(min_dist) and target_diff > min_dist): 
                min_dist = target_diff
            
            if target_diff > 0: 
                left += 1 
            else: 
                right -= 1 
    return target_sum - min_dist

assert searchTriplet([-1, 0, 2, 3], 3) == 2
assert searchTriplet([-3, -1, 1, 2], 1) == 0 
assert searchTriplet([1, 0, 1, 1], 100) == 3 
assert searchTriplet([0, 0, 1, 1, 2, 6], 5) == 4
