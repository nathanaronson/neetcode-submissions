class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            i = ord(c) - ord('a')
            if not curr.children[i]:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        
        curr.word = True

    def search(self, word: str) -> bool:
        return self._dfs(word, self.root)
    
    def _dfs(self, suffix: str, node: TrieNode) -> bool:
        if not node:
            return False

        if len(suffix) == 0:
            return node.word
        
        if suffix[0] == '.':
            return any([self._dfs(suffix[1:], child) for child in node.children])
        else:
            i = ord(suffix[0]) - ord('a')
            return self._dfs(suffix[1:], node.children[i])