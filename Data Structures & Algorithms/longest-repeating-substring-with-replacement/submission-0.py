class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        have = defaultdict(int)
        for r in range(len(s)):
            have[s[r]] += 1
            size = r - l + 1
            freq = 0
            freq = max(have.values())
            while (size - freq) > k:
                have[s[l]] -= 1
                l += 1
                size = r - l + 1
                freq = max(have.values())
            res = max(size,res)
        return res