def connected_components(graph): 
    count = 0 
    visited = set()

    for n in graph: # this is all the keys
        if dfs(graph, n, visited):
            count += 1
    return count  

def dfs(graph, current, visited): 
    if current in visited: 
        return False
    visited.add(current)
    for n in graph[current]:
        dfs(graph, n, visited)
    return True 