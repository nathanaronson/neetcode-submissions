class Solution:
    def numDecodings(self, s: str) -> int:
        # G(i) = num ways to decode from s[i:]
        # G(n) = 1
        # G(i) = 0 if s[i] = 0
        # G(i) = dp[i + 1] + dp[i + 2] if valid

        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 1

        for i in range(n - 1, -1 , -1):
            if s[i] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]
                if i + 1 < n and int(s[i : i + 2]) <= 26:
                    dp[i] += dp[i + 2]
        
        return dp[0]