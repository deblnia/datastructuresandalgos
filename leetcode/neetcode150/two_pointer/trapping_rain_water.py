
def trap(height: list[int]) -> int:
    if not height:
        return 0

    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]

    res = 0
    while left < right:
        left_max, right_max = max(height[left], left_max), max(height[right], right_max)
        if height[left] < height[right]:
            res += left_max - height[left]
            left += 1
        else:
            res += right_max - height[right]
            right -= 1
    return res

assert trap([0,2,0,3,1,0,1,3,2,1]) == 9
