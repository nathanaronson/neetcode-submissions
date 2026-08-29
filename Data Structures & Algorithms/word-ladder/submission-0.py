class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList) | {beginWord}
        wordDict = defaultdict(list)

        for word in words:
            for i in range(len(word)):
                for j in range(ord('a'), ord('z') + 1):
                    candidate = word[:i] + chr(j) + word[i + 1:]
                    if candidate in words and candidate != word:
                        wordDict[word].append(candidate)
                
        queue = deque()
        visited = set()
        depth = 1

        queue.append(beginWord)
        visited.add(beginWord)

        while queue:
            size = len(queue)
            depth += 1
            print(queue)
            for i in range(size):
                word = queue.popleft()

                for other in wordDict[word]:
                    if other == endWord:
                        return depth

                    if other not in visited:
                        visited.add(other)
                        queue.append(other)

        return 0