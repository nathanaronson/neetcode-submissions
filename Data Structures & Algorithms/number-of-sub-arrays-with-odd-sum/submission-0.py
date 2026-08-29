class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        total = 0
        prefix = []
        even, odd, count = 0, 0, 0

        # 1, 3, 5
        # 1, 4, 9

        for num in arr:
            total += num
            prefix.append(total)
            if total % 2 == 1:
                odd += 1
                count += 1 % MOD
                count += even % MOD
            else:
                even += 1
                count += odd % MOD
        
        return count
