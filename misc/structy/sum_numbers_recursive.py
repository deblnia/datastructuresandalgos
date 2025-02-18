def sum_numbers_recursive(nums):
    if not nums: 
        return 0 
    curr = nums.pop(0)
    return curr + sum_numbers_recursive(nums)

assert sum_numbers_recursive([5, 2, 9, 10]) == 26
assert sum_numbers_recursive([1, -1, 1, -1, 1, -1, 1]) == 1
assert sum_numbers_recursive([]) == 0
assert sum_numbers_recursive([1000, 0, 0, 0, 0, 0, 1]) == 1001
assert sum_numbers_recursive([700, 70, 7]) == 777



