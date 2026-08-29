class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()

        adj = [[] for _ in range(numCourses)]

        for u, v in prerequisites:
            adj[u].append(v)

        def dfs(course):
            visited.add(course)
            for neighbor in adj[course]:
                if neighbor in visited or not dfs(neighbor):
                    return False
            
            visited.discard(course)
            adj[course].clear()
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True