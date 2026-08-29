class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)
    
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        a, b = self.find(x), self.find(y)

        if a == b:
            return False

        if self.rank[a] < self.rank[b]:
            a, b = b, a
        
        self.parent[b] = a

        if self.rank[a] == self.rank[b]:
            self.rank[a] += 1
        
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges))

        for u, v in edges:
            if not dsu.union(u, v):
                return [u, v]