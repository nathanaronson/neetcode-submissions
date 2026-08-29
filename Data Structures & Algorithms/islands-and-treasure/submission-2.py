class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2 ** 31 - 1
        m, n = len(grid), len(grid[0])

        queue = deque()
        visited = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append((i, j))
                    visited.add((i, j))

        distance = 0

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def is_valid(r, c):
            nonlocal m, n, visited, grid, INF
            return r >= 0 and r < m and c >= 0 and c < n and (r, c) not in visited and grid[r][c] == INF

        while queue:
            size = len(queue)

            for i in range(size):
                r, c = queue.popleft()
                grid[r][c] = distance
                for y, x in directions:
                    if is_valid(r + y, c + x):
                        queue.append((r + y, c + x))
                        visited.add((r + y, c + x))
                
            distance += 1
                
