class Solution:
    def trap(self, height: List[int]) -> int:
        min_heights = []
        cur = 0
        for h in height:
            min_heights.append(cur)
            cur = max(cur,h)
        cur = 0
        for i in range(len(height) - 1,-1,-1):
            min_heights[i] = min(min_heights[i],cur)
            cur = max(height[i],cur)
        res = 0
        for i in range(len(height)):
            res += max(0,min_heights[i] - height[i])
        return res