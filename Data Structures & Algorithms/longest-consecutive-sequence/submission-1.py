class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0

        for i in s:
            if i - 1 in s:
                continue
            curr = 0
            j = i
            while j in s:
                j = j + 1
                curr = curr + 1
            longest = max(longest, curr)
        
        return longest
            