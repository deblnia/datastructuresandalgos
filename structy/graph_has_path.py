def has_path(graph, src, dst: 
    """
    This is the DFS implmenetation. 
    """
    if src == dst:  # type: ignore
        return True 
    for neigh in graph[src]: 
        if has_path(graph, neigh, dst):
            return True 
    return False