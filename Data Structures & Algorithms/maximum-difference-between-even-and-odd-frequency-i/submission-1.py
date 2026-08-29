class Solution:
    def maxDifference(self, s: str) -> int:
        c = Counter(s)

        min_even, max_odd = float('inf'), 0
        for f in c.values():
            if f % 2 == 0 and f < min_even:
                min_even = f
            elif f % 2 == 1 and f > max_odd:
                max_odd = f
        
        return max_odd - min_even