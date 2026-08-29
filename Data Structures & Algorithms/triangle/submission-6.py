class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # G(i) = minimum total sum ending at position j of row i
        n = len(triangle)
        dp = [0] * n

        for i in range(n):
            dp[i] = triangle[n - 1][i]
        
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])

        return dp[0]