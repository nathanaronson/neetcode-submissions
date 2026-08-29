import bisect

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = bisect.bisect_left(nums, target), bisect.bisect_right(nums, target) - 1
        if l > r:
            return [-1, -1]
        return [l, r]
