class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        for (a, b), val in zip(equations, values):
            graph[a].append((b, val))
            graph[b].append((a, 1 / val))
        
        def dfs(curr, target, seen):
            if curr == target:
                return 1.0
            
            seen.add(curr)

            for v, w in graph[curr]:
                if v not in seen:
                    res = dfs(v, target, seen)
                    if res != -1:
                        return w * res
            
            return -1
        
        res = []

        for a, b in queries:
            if a not in graph or b not in graph:
                res.append(-1.0)
            else:
                res.append(dfs(a, b, set()))
        
        return res
