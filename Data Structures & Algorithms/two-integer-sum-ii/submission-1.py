class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def binary_search(l,num):
            r = len(numbers) - 1
            while l <= r:
                mid = (l + r) // 2
                if numbers[mid] == num:
                    return mid
                if numbers[mid] > num:
                    r = mid - 1
                else:
                    l = mid + 1
            return None

        for i,n in enumerate(numbers):
            looking_for = target - n
            res = binary_search(i + 1,looking_for)
            if res != None:
                return [i + 1,res + 1]