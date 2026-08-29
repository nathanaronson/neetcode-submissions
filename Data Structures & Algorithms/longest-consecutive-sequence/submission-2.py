class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        best = 0

        for num in nums:
            if num - 1 in nums:
                continue
            
            streak = 0
            while num + streak in nums:
                streak += 1
            
            best = max(best, streak)
        
        return best