class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + '#' + s

        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            l = ''
            while s[i] != '#':
                l += s[i]
                i += 1
            temp = ''
            for _ in range(int(l)):
                i += 1
                temp += s[i]
            res.append(temp)
            i += 1
        return res
