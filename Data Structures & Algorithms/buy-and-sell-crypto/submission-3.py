class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        res = 0
        for r in range(1,len(prices)):
            price = prices[l]
            res = max(res,prices[r] - price)
            if prices[r] < price:
                l = r
        return res
