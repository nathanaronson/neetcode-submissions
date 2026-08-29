class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        cur = 0
        for num in nums:
            cur += num
            res = max(res, cur)
            cur = max(0, cur)
        
        return res
