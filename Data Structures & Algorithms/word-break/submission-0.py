class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # G(i) = s[i:] can be segmented into a space-separated sequence
        # G(n) = true 
        # G(i) = any(for word in words, word is a prefix and remaining G(j) is true)
        # return G(0)
        n = len(s)

        dp = [False] * (n + 1)
        dp[n] = True

        for i in range(n - 1, -1, -1):
            dp[i] = any(
                i + len(word) <= n and s[i : i + len(word)] == word and dp[i + len(word)]
                for word in wordDict
            )
        
        return dp[0]