class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(set)
        
        for u, v in prerequisites:
            adj[u].add(v)

        dependencies = [set() for _ in range(numCourses)]

        def dfs(src, v):
            for u in adj[v]:
                if u not in dependencies[src]:
                    dependencies[src].add(u)
                    dfs(src, u)

        for i in range(numCourses):
            dfs(i, i)

        return [v in dependencies[u] for u, v in queries]