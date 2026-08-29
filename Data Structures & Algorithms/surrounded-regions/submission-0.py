class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # Multisource BFS from Each Edge O:
        # Mark Visited as Y
        # Swap Each O to X and Y to O

        DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))
        m, n = len(board), len(board[0])
        queue = deque()

        for i in range(m):
            if board[i][0] == 'O':
                queue.append((i, 0))
                board[i][0] = 'Y'
            if board[i][n - 1] == 'O':
                queue.append((i, n - 1))
                board[i][n - 1] = 'Y'
        
        for i in range(n):
            if board[0][i] == 'O':
                queue.append((0, i))
                board[0][i] = 'Y'
            if board[m - 1][i] == 'O':
                queue.append((m - 1, i))
                board[m - 1][i] = 'Y'

        while queue:
            r, c = queue.popleft()
            neighbors = [(r + dr, c + dc) for dr, dc in DIRS if 0 <= r + dr < m and 0 <= c + dc < n]

            for nr, nc in neighbors:
                if board[nr][nc] == 'O':
                    board[nr][nc] = 'Y'
                    queue.append((nr, nc))
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'Y':
                    board[i][j] = 'O'