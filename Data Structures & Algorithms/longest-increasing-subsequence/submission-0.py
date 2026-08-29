class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
       n = len(nums)
       dp = [1] * n

       for i in range(1, n):
           optimal = 0
           for j in range(0, i):
               if nums[j] < nums[i]:
                   optimal = max(optimal, dp[j])
           dp[i] += optimal

       return max(dp)
