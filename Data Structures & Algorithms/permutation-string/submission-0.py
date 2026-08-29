class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False

        c1 = Counter(s1)
        c2 = Counter(s2[:n])

        for i in range(n, m):
            if c1 == c2:
                return True
            
            c2[s2[i]] += 1
            c2[s2[i - n]] -= 1

        return c1 == c2