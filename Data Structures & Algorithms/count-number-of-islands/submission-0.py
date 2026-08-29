class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    grid[i][j] = "0"
                    res += 1
                    queue = []
                    queue.append((i, j))
                    while queue:
                        i, j = queue.pop(0)
                        if i > 0 and grid[i - 1][j] == "1":
                            queue.append((i - 1, j))
                            grid[i-1][j] = "0"
                        if i < n - 1 and grid[i + 1][j] == "1":
                            queue.append((i + 1, j)) 
                            grid[i+1][j] = "0"   
                        if j > 0 and grid[i][j - 1] == "1":
                            queue.append((i, j - 1))
                            grid[i][j-1] = "0"
                        if j < m - 1 and grid[i][j + 1] == "1":
                            queue.append((i, j + 1))
                            grid[i][j+1] = "0"  
        
        return res