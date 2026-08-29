class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        return [x for x, y in freq.items() if y > len(nums) // 3]