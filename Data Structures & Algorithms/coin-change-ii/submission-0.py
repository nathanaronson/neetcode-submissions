class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # G(i) = numbers of distinct combinations that total up to i
        # G(0) = 1
        # G(i) = \sum_{coin in Coins} G(i - coin)
        # return G(amount)
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]

        return dp[amount]