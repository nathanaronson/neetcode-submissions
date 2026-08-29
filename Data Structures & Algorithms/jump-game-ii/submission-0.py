class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        prev, best = -1, 0
        curr = 0

        while best < len(nums) - 1:
            for i in range(prev + 1, best + 1):
                curr = max(curr, i + nums[i])
            best = curr
            jumps += 1

        return jumps