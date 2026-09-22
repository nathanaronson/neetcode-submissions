class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        path = set()

        def dfs(r, c, l):            
            if board[r][c] != word[l]:
                return False
            
            l += 1
            
            if l == len(word):
                return True
            
            path.add((r, c))
            
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in path:
                    if dfs(nr, nc, l):
                        return True
            
            path.discard((r, c))
            return False

        return any(dfs(i, j, 0) for i in range(m) for j in range(n))