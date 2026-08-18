class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = []
        res = 0
        for num in prices:
            while stack and stack[-1] > num:
                res = max(res,stack[-1] - stack[0])
                stack.pop()
            stack.append(num)

        return max(res,stack[-1] - stack[0])