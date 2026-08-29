class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # G(i) = fewest amount of coins to yield i total
        # G(0) = 0
        # G(i) = min j s.t. coins[j] exists: G(i - coins[j]) + 1

        dp = [0] * (amount + 1)
        for coin in coins:
            if coin <= amount:
                dp[coin] = 1

        print(dp)
        for i in range(amount + 1):
            if dp[i] == 1:
                continue
            dp[i] = min([dp[i - coin] + 1 for coin in coins if i - coin >= 0 and dp[i - coin] > 0], default = 0)
        
        return dp[amount] if dp[amount] > 0 or amount == 0 else -1