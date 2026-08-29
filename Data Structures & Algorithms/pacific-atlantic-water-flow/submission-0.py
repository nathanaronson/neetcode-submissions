class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        def get_neighbors(r, c):
            neighbors = []
            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in dirs:
                i, j = r + dr, c + dc
                if 0 <= i < m and 0 <= j < n:
                    neighbors.append((i, j))
            return neighbors

        def get_reachable(queue):
            visited = set(queue)

            while queue:
                r, c = queue.popleft()

                for i, j in get_neighbors(r, c):
                    if heights[i][j] >= heights[r][c] and (i, j) not in visited:
                        visited.add((i, j))
                        queue.append((i, j))

            return visited

        pacific_sources = deque()
        atlantic_sources = deque()

        for i in range(n):
            pacific_sources.append((0, i))
            atlantic_sources.append((m - 1, i))

        for i in range(m):
            pacific_sources.append((i, 0))
            atlantic_sources.append((i, n - 1))

        pacific_reachable = get_reachable(pacific_sources)
        atlantic_reachable = get_reachable(atlantic_sources)

        return [list(cell) for cell in pacific_reachable & atlantic_reachable]