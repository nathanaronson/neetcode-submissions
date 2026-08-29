class Solution {
public:
    int climbStairs(int n) {
        // G(1) = 1
        // G(i) = G(i - 1) + G(i - 2)
        // Return: G(n)

        if (n == 1) return 1;
        vector<int> dp(n + 1);
        dp[0] = 1;
        dp[1] = 1;

        for (int i = 2; i <= n; ++i) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }

        return dp[n];
    }
};
