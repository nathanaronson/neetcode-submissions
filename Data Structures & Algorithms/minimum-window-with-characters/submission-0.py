class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n, m = len(s), len(t)
        l_best, r_best, size = 0, 0, n + 1
        l = r = 0
        have = set()
        ct = Counter(t)
        cs = Counter()

        for r in range(n):
            cs[s[r]] += 1
            if cs[s[r]] >= ct[s[r]] and ct[s[r]] > 0:
                have.add(s[r])
            if len(have) < len(ct.keys()):
                continue
            while len(have) == len(ct.keys()):
                cs[s[l]] -= 1
                if cs[s[l]] < ct[s[l]] and ct[s[r]] > 0:
                    have.remove(s[l])
                l += 1
            if r - l + 2 < size:
                size = r - l + 2
                l_best = l - 1
                r_best = r + 1
        
        return "" if size == n + 1 else s[l_best:r_best]