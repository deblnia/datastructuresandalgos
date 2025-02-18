from collections import deque 
def shortest_path(edges, node_A, node_B):
  # convert into graph adj list 
  graph = build_graph(edges) 
  visited = set([ node_A ])
  q = deque([ (node_A , 0) ])

  # breadth first traversal - using queue, and set of visited
  while q: 
    node, distance = q.popleft()
    # starting node, 0 = current
    if node == node_B:
      return distance 
    # explore neighbors, adding to q with increment distance
    for neighbor in graph[node]: 
      if neighbor not in visited: 
        visited.add(neighbor)
        q.append((neighbor, distance + 1))
  return -1 

def build_graph(edges):
  graph = {}
  for edge in edges: 
    a , b = edge # can destructre list 
    if a not in graph:
      graph[a] = []
    if b not in graph:
      graph[b] = []

    graph[a].append(b)
    graph[b].append(a)
  return graph 