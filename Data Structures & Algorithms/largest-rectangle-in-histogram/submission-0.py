class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        for i,h in enumerate(heights):
            index = i
            while stack and stack[-1][0] > h:
                height,index = stack.pop()
                area = (i - index) * height
                res = max(res,area)
            stack.append([h,index])
        
        for h,i in stack:
            area = (len(heights) - i) * h
            res = max(res,area)
        return res