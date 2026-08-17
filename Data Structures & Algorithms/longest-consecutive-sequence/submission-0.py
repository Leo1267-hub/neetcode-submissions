class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums = set(nums)
        for num in nums:
            if num - 1 not in nums:
                s = 1
                while True:
                    if num + 1 in nums:
                        s += 1
                        num = num + 1
                    else:
                        break
                res = max(res,s)
        return res
                