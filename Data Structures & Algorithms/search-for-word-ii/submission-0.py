class TrieNode:
    def __init__(self, is_word = False, word = None):
        self.children = [None] * 26
        self.word = word

class PrefixTrie:
    def __init__(self, words):
        self.root = TrieNode()
    
        for word in words:
            self.insert(word)
    
    def insert(self, word):
        node = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not node.children[idx]:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        
        node.word = word
    
    def get_child(self, node, c):
        return node.children[ord(c) - ord('a')]
    
    def get_word(self, node):
        return node.word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        trie = PrefixTrie(words)
        m, n = len(board), len(board[0])
        found = set()

        def dfs(node, r, c):
            char = board[r][c]
            child = trie.get_child(node, char)
            if not child:
                return

            word = trie.get_word(child)
            if word:
                found.add(word)

            board[r][c] = '#'
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] != '#':
                    dfs(child, nr, nc)
            board[r][c] = char

        for i in range(m):
            for j in range(n):
                dfs(trie.root, i, j)

        return list(found)