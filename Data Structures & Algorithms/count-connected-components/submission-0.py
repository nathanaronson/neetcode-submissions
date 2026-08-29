class DSU:
    def __init__(self, n):
        self.cc = n
        self.parent = list(range(n))
        self.rank = [1] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        p1, p2 = self.find(x), self.find(y)

        if p1 == p2:
            return
        
        if self.rank[p1] < self.rank[p2]:
            p1, p2 = p2, p1
        
        self.parent[p2] = p1

        if self.rank[p1] == self.rank[p2]:
            self.rank[p1] += 1
        
        self.cc -= 1


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)

        for u, v in edges:
            dsu.union(u, v)
        
        return dsu.cc