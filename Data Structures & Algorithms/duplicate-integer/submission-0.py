class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        have = set()
        for i in nums:
            if i in have:
                return True
            have.add(i)
        return False