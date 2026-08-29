class Solution:
    def numDecodings(self, s: str) -> int:
        # G(i) = num ways to decode from s[i:]
        # G(n) = 1
        # G(i) = 0 if s[i] = 0
        # G(i) = dp[i + 1] + dp[i + 2] if valid

        n = len(s)
        curr, prev = 1, 0

        for i in range(n - 1, -1 , -1):
            if s[i] == '0':
                prev = curr
                curr = 0
            else:
                temp = curr
                if i + 1 < n and int(s[i : i + 2]) <= 26:
                    temp += prev
                
                prev = curr
                curr = temp
        
        return curr