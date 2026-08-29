class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # dp[i][j] = dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1] + matrix[i][j]
        m, n = len(matrix), len(matrix[0])
        self.dp = [[0] * n for _ in range(m)]
    
        for i in range(m):
            for j in range(n):
                a = self.dp[i][j - 1] if j > 0 else 0
                b = self.dp[i - 1][j] if i > 0 else 0
                c = self.dp[i - 1][j - 1] if i > 0 and j > 0 else 0
                self.dp[i][j] = a + b - c + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        a = self.dp[row1 - 1][col2] if row1 > 0 else 0
        b = self.dp[row2][col1 - 1] if col1 > 0 else 0
        c = self.dp[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0
        return self.dp[row2][col2] - a - b + c


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)