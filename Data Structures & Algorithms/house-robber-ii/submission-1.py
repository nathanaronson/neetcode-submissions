class Solution:
    def rob(self, nums: List[int]) -> int:
        # try to rob starting at nums[0] and nums[1]

        prev = curr = best_0 = 0

        for i in range(0, len(nums) - 1):
            best_0 = max(prev + nums[i], curr)
            prev = curr
            curr = best_0
        
        prev = curr = best_1 = 0
        for i in range(1, len(nums)):
            best_1 = max(prev + nums[i], curr)
            prev = curr
            curr = best_1
        
        return max(nums[0], max(best_0, best_1))