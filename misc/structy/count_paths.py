def count_paths(grid):
  return _count_paths(grid, 0, 0, {})

def _count_paths(grid, r, c, memo):
  pos = (r, c)
  if pos in memo:
    return memo[pos]
  
  if r == len(grid) or c == len(grid[0]) or grid[r][c] == 'X':
    return 0
  
  if r == len(grid) - 1 and c == len(grid[0]) - 1:
    return 1
  
  memo[pos] = _count_paths(grid, r + 1, c, memo) + _count_paths(grid, r, c + 1, memo)
  return memo[pos]
# not sure what the brute force is here - you'll need a helper function either way right? 