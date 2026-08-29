class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1

        while True:
            m = (l + r) // 2
            mid = nums[m]
            left = nums[m - 1] if m > 0 else float('-inf')
            right = nums[m + 1] if m < n - 1 else float('-inf')
            if left < mid and mid > right:
                return m
            elif left < mid and mid < right:
                l = m + 1
            else:
                r = m - 1