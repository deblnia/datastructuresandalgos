from typing import List 
def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    # need this so that even courses without prereqs are in the list 
    adjacency_list = {i: [] for i in range(numCourses)}
    for pair in prerequisites:
        adjacency_list[pair[0]].append(pair[1])
    
    visiting = set()
    def dfs(course):
        if course in visiting: 
            return False 
        if adjacency_list[course] == []: 
            return True 
        visiting.add(course)
        for pre_req in adjacency_list[course]: 
            if not dfs(pre_req): return False 
        visiting.remove(course)
        adjacency_list[course] = []
        return True 
    
    for course in range(numCourses): 
        if not dfs(course): return False 
    return True 



assert canFinish(2, [[1,0]]) == True 
assert canFinish(2, [[1,0], [0,1]]) == False