class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        mask = 1

        for i in range(32):
            if mask & n:
                count += 1
            mask <<= 1
        
        return count