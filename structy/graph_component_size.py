def largest_component(graph):
  curr_max_size = 0 
  visited = set()
  for node in graph:
    size = get_size(graph, node, visited)
    curr_max_size = max(size, curr_max_size)
  return curr_max_size

def get_size(graph, node, visited):
  if node in visited: 
    return 0
  visited.add(node)
  size = 1 
  for nei in graph[node]:
    size += get_size(graph, nei, visited)
  return size 