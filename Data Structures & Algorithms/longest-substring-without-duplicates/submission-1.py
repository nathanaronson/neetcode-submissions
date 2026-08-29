class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = res = 0
        curr = set()
        while r < len(s):
            if s[r] in curr:
                while s[l] != s[r]:
                    curr.remove(s[l])
                    l += 1
                l += 1
            curr.add(s[r])
            r += 1
            res = max(res, r - l)

        return res

        # r = 3, l = 0