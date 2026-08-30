class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row_sum, col_sum = [sum(row) for row in grid], [sum(col) for col in zip(*grid)]
        m, n = len(grid), len(grid[0])
        return sum([int(grid[i][j] == 1 and (row_sum[i] > 1 or col_sum[j] > 1)) for i in range(m) for j in range(n)])