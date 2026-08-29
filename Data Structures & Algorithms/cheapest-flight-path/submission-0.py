class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]

        for u, v, w in flights:
            adj[v].append((u, w))

        dp = [[float('inf')] * n for _ in range(k + 2)]
        dp[0][src] = 0

        for i in range(1, k + 2):
            for j in range(n):
                dp[i][j] = min(min([dp[i - 1][v] + w for v, w in adj[j]], default = float('inf')), dp[i - 1][j])
            
        print(dp)

        return int(dp[k + 1][dst]) if not math.isinf(dp[k + 1][dst]) else -1