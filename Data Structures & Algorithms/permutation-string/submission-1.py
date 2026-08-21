class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        c1 = Counter(s1)
        c2 = Counter()
        l1 = len(s1)
        l = 0
        for r in range(len(s2)):
            c2[s2[r]] += 1
            if l1 != r - l + 1:
                continue
            if c2 == c1:
                return True
            c2[s2[l]] -= 1
            l += 1
        return False