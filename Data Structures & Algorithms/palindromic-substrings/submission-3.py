class Solution:
    def countSubstrings(self, s: str) -> int:
        # G(i, j) = s[i:j] is a palindrome
        # G(i, j) = s[i] == s[j] and G(i + 1, j - 1)
        
        n, res = len(s), 0
        dp = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    res += 1
        
        return res