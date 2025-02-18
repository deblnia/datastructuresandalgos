"""
My solution is hackier. The key is to be backwards looking in the loop.
"""

# class Solution:
#   def moveElements(self, arr):
#     l = 0
#     for i, v in enumerate(arr):
#       if i == 0:
#         continue 
#       if v != arr[i - 1]:
#         arr[l] = v
#         l += 1 
#     return l+1

class Solution:
  def moveElements(self, arr):
    next_non_duplicate = 1
    i = 0

    while i < len(arr):
      # Check if the current element is different from the previous element
      if arr[next_non_duplicate - 1] != arr[i]:
        # If different, put the element at the next_non_duplicate position 
        arr[next_non_duplicate] = arr[i]
        next_non_duplicate += 1
      i += 1
    return next_non_duplicate



