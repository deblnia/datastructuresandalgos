def build_graph(edges): 
    graph = {}

    for edge in edges: 
        a, b = edge 
        if a not in graph: 
            graph[a] = []
        if b not in graph:
            graph[b] = []
        
        graph[a].append(b)
        graph[b].append(a)
    return graph 

def has_path_dfs(graph, src, dst, visited): 
    if src == dst: 
        return True 
    
    if src in visited: 
        return False 
    
    visited.add(src)
    
    for n in graph[src]: 
        if has_path_dfs(graph, n, dst, visited) == True: 
            return True 
    return False 

def undirected_path(edges, node_A, node_B): 
    graph = build_graph(edges)
    return has_path_dfs(graph, node_A, node_B, set())