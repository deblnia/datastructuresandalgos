# both of these are O(num. edges) time and O(n) space 

def has_path(graph, src, dst): 
    """
    This is the DFS implmenetation. 
    """
    if src == dst:  # type: ignore
        return True 
    for neigh in graph[src]: 
        if has_path(graph, neigh, dst):
            return True 
    return False

from collections import deque 

def has_path_bfs(graph, src, dst): 
    q = deque([ src ])

    while q: 
        curr = q.popleft()
    if curr == dst: 
        return True 
    for neigh in graph[curr]: 
        q.append(neigh) 
    return False 