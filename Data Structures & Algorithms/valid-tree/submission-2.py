class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
       # n - 1 edges
       # dfs on random node visits everything

       if len(edges) != n - 1:
           return False

       adj = [[] for _ in range(n)]

       for u, v in edges:
           adj[u].append(v)
           adj[v].append(u)

       visited = [False] * n

       def dfs(x):
           visited[x] = True

           for y in adj[x]:
               if not visited[y]:
                   dfs(y)
      
       dfs(0)
       return all(visited)
