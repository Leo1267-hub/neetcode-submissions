class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l,r = 0,len(height) -1
        maxLeft = height[l]
        maxRight = height[r]
        while l < r:
            if height[l] > height[r]:
                res += max(0,maxRight - height[r])
                r -= 1
                maxRight = max(maxRight,height[r])
            else:
                res += max(0,maxLeft - height[l])
                l += 1
                maxLeft = max(maxLeft,height[l])
        return res
            