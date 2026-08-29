class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total // 2

        dp = {0}

        for stone in stones:
            dp |= {stone + s for s in dp if stone + s <= target}
        
        best = max(dp)
        return total - 2 * best