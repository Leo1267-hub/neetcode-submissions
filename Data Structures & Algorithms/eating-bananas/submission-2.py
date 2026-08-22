class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,max(piles)
        res = r
        while l <= r:
            poss_k = (r + l) // 2
            time = 0
            for pile in piles:
                time += math.ceil(pile / poss_k)
            if time <= h:
                res = poss_k
                r = poss_k - 1
            else:
                l = poss_k + 1
        return res