
def maxArea(heights: list[int]) -> int:
    l, r = 0, len(heights) - 1
    max_area = 0
    while l < r:
        area = (r - l) * min(heights[l], heights[r])
        max_area = max(max_area, area)
       # always want to update the smallest bar since that's the limiter 
	if heights[l] < heights[r]:
            l += 1
        else:
            r -= 1
    return max_area


assert maxArea([1,7,2,5,4,7,3,6]) == 36
assert maxArea([2,2,2]) == 4
