class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)

        lo, hi = max(nums), sum(nums)
        best = hi
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            
            current_sum, splits = 0, 1
            for num in nums:
                current_sum += num
                if current_sum > mid:
                    current_sum = num
                    splits += 1
            
            if splits > k:
                lo = mid + 1
            else:
                hi = mid - 1
                best = mid
        
        return best
