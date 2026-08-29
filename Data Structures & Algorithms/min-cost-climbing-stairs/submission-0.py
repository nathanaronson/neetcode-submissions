class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # G(i) = min cost of climbing to stair i
        # G(i) = min (G(i - 1) + cost[i - 1], G(i - 2) + cost[i - 2])
        # G(0) = G(1) = 0
        dp_1, dp_2 = 0, 0
        for i in range(2, len(cost) + 1):
            dp_0 = min(dp_1 + cost[i - 1], dp_2 + cost[i - 2])
            dp_2 = dp_1
            dp_1 = dp_0
        
        return dp_1