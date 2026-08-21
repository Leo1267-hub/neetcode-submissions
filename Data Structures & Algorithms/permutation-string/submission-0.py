class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        c1 = Counter(s1)
        l1 = len(s1)
        for i in range(len(s2)):
            if i + l1 > len(s2):
                break
            if Counter(s2[i:i + l1]) == c1:
                return True
        return False