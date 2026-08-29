class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # 553
        # 236
        # 111
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        m, n = len(matrix), len(matrix[0])
        dp = [[-1] * n for _ in range(m)]
        result = -1

        def dfs(r, c):
            if dp[r][c] != -1:
                return dp[r][c]
            
            neighbors = []

            for dr, dc in DIRS:
                y, x = r + dr, c + dc
                if 0 <= y < m and 0 <= x < n and matrix[y][x] > matrix[r][c]:
                    neighbors.append(dfs(y, x))
                            
            dp[r][c] = 1 + max(neighbors, default = 0)
            return dp[r][c]
        
        return max([dfs(r, c) for r in range(m) for c in range(n)])
