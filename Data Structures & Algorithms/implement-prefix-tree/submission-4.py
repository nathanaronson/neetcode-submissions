class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.word = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            i = self._get_idx(c)
            if not curr.children[i]:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        
        curr.word = True

    def search(self, word: str) -> bool:
        res = self._traverse(word)
        return res.word if res else False

    def startsWith(self, prefix: str) -> bool:
        return self._traverse(prefix) is not None
    
    def _get_idx(self, c):
        return ord(c) - ord('a')
    
    def _traverse(self, word):
        curr = self.root

        for c in word:
            i = self._get_idx(c)
            if not curr.children[i]:
                return None
            curr = curr.children[i]
        
        return curr