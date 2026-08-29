class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total / 2

        dp = set()

        for num in nums:
            to_add = {num}
            for val in dp:
                to_add.add(val + num)
            dp = dp | to_add
        
        return True if target in dp else False