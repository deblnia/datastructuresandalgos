
def twoSum(numbers: list[int], target: int) -> list[int]:
    l, r = 0, len(numbers) - 1
    while l < r:
        if numbers[l] + numbers[r] == target:
            return [l+1, r+1]
        elif numbers[l] + numbers[r] < target:
            l += 1
        else:
            r -= 1
    return []


assert twoSum([1,2,3,4], 3) == [1,2]
