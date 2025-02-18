
# Given an array arr of unsorted numbers and a target sum, count all triplets in it such that
# arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices.
# Write a function to return the count of such triplets.
# If no such triplets exist, return 0.
# Time complexity: O(n^2)
# Space complexity: O(n)

def searchTriplets(arr:list[int], target:int)->int:
    arr.sort()
    count = 0
    for i in range(len(arr) - 2):
        left, right = i + 1, len(arr) - 1
        while left < right:
            if arr[i] + arr[left] + arr[right] < target:
            # If the sum is less than the target, all elements between left and right
            # will also form a valid triplet with arr[i] and arr[left].
                count += right - left
                left += 1
            else: right -= 1
    return count


assert searchTriplets([-1, 0, 2, 3], target=3) == 2
assert searchTriplets([-1, 4, 2, 1, 3], target=5) == 4
