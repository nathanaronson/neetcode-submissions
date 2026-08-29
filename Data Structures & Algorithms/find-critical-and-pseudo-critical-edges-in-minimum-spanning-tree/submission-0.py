class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        root = x
        while self.parent[root] != root:
            root = self.parent[root]
        while self.parent[x] != root:
            self.parent[x], x = root, self.parent[x]
        return root
    
    def union(self, x, y):
        p1, p2 = self.find(x), self.find(y)

        if p1 == p2:
            return False
        
        if self.rank[p2] > self.rank[p1]:
            p1, p2 = p2, p1
        
        self.parent[p2] = p1

        if self.rank[p1] == self.rank[p2]:
            self.rank[p1] += 1
        
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        idx = sorted(range(len(edges)), key=lambda i: edges[i][2])

        def mst(skip = -1, force = -1):
            dsu = DSU(n)
            w = 0
            cnt = 0
            if force != -1:
                a, b, wt = edges[force]
                dsu.union(a, b)
                w += wt
                cnt += 1
            for i in idx:
                if i == skip:
                    continue
                a, b, wt = edges[i]
                if dsu.union(a, b):
                    w += wt
                    cnt += 1
            return w if cnt == n - 1 else float('inf')

        base = mst()
        crit, pseudo = [], []
        for i in range(len(edges)):
            if mst(skip=i) > base:
                crit.append(i)
            elif mst(force=i) == base:
                pseudo.append(i)
        return [crit, pseudo]
        