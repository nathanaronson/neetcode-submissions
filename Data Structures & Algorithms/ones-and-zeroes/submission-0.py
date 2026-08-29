class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = {(0, 0, 0)}

        for s in strs:
            freq = Counter(s)
            dp |= {(a + freq['0'], b + freq['1'], c + 1) for a, b, c in dp if a + freq['0'] <= m and b + freq['1'] <= n}
        
        return max(c for _, _, c in dp)