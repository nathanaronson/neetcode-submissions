class DSU:
    def __init__(self, n):
        self.provinces = n
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def get_provinces(self):
        return self.provinces
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        p_x, p_y = self.find(x), self.find(y)

        if p_x == p_y:
            return
        
        if self.rank[p_y] > self.rank[p_x]:
            p_x, p_y = p_y, p_x
        
        self.parent[p_y] = p_x
        self.provinces -= 1

        if self.rank[p_x] == self.rank[p_y]:
            self.rank[p_x] += 1

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        dsu = DSU(n)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    dsu.union(i, j)
        
        return dsu.get_provinces()