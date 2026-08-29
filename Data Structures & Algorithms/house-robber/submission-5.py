class Solution:
    def rob(self, nums: List[int]) -> int:
        prev = curr = 0

        for num in nums:
            choice = max(curr, prev + num)
            prev = curr
            curr = choice
        
        return curr