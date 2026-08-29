class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = res = 0
        freq = [0] * 26

        while r < len(s):
            freq[ord(s[r]) - ord('A')] += 1
            common = max(freq)
            while r - l + 1 - common > k:
                freq[ord(s[l]) - ord('A')] -= 1
                l += 1
                common = max(freq)
            res = max(res, r - l + 1)
            r += 1
        
        return res
