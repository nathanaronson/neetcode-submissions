class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = deque()
        fresh = 0

        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        time = 0

        while rotten and fresh > 0:
            size = len(rotten)
            
            for i in range(size):
                r, c = rotten.popleft()

                for u, v in self._neighbors(r, c, m, n):
                    if grid[u][v] == 1:
                        grid[u][v] = 2
                        fresh -= 1
                        rotten.append((u, v))

            time += 1
        
        return -1 if fresh > 0 else time

    def _neighbors(self, r, c, m, n):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        res = []

        for dr, dc in directions:
            x, y = r + dr, c + dc
            if x >= 0 and x < m and y >= 0 and y < n:
                res.append((x, y))

        return res
