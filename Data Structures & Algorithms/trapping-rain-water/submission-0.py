class Solution:
    def trap(self, height: List[int]) -> int:
        prefix, suffix = list(accumulate(height, max)), list(accumulate(reversed(height), max))[::-1]
        return sum([min(prefix[i], suffix[i]) - height[i] for i in range(1, len(height) - 1)])