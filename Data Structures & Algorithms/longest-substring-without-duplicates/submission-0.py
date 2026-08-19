class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        have = set()
        res = 0
        l = 0
        for r in range(len(s)):
            char = s[r]
            while char in have:
                have.remove(s[l])
                l += 1
            have.add(char)
            res = max(res, (r - l + 1))
        return res