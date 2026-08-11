class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        have = {}
        for i,num in enumerate(nums):
            need = target - num
            if need in have:
                return [have[need],i]
            have[num] = i