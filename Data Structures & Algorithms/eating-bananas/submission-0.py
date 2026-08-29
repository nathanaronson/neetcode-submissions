class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        result = hi

        while lo <= hi:
            k = lo + (hi - lo) // 2
            hours = sum([-(-pile // k) for pile in piles])
            if hours <= h:
                res = k
                hi = k - 1
            else:
                lo = k + 1
        
        return res