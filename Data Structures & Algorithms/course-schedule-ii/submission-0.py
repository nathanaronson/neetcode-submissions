class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]

        for u, v in prerequisites:
            adj[u].append(v)
        
        result = []
        discovered = set()
        processing = set()

        def dfs(u):            
            if u in processing:
                return False

            if u in discovered:
                return True

            discovered.add(u)
            processing.add(u)

            for v in adj[u]:
                if not dfs(v):
                    return False
            
            processing.discard(u)
            result.append(u)

            return True
        
        return [] if any([not dfs(i) for i in range(numCourses)]) else result