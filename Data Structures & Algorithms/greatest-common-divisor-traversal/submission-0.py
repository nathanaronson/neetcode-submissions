class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
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
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        dsu = DSU(n)
        seen = {}

        for i, num in enumerate(nums):
            for p in self._prime_factors(num):
                if p not in seen:
                    seen[p] = i
                else:
                    dsu.union(i, seen[p])
        
        root = dsu.find(0)

        return all(dsu.find(i) == root for i in range(n))

    def _prime_factors(self, x):
        factors = []
        p = 2

        while p * p <= x:
            if x % p == 0:
                factors.append(p)
                while x % p == 0:
                    x //= p
            p += 1

        if x > 1:
            factors.append(x)

        return factors