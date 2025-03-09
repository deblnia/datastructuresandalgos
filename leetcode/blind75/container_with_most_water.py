def maxArea(height: list[int]) -> int:
    l, r = 0, len(height) - 1 
    max_area = float('-Inf') # could also be 0 
    while l < r: 
        tmp_area = min(height[l], height[r]) * (r - l)
        max_area = max(max_area, tmp_area)
        if height[l] < height[r]: 
            l += 1 
        else: 
            r -= 1
    return max_area 

assert maxArea([1,8,6,2,5,4,8,3,7]) == 49 