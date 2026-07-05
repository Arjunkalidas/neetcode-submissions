class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                if nums[i] == nums[j]:
                    nums[i], nums[j] = 2147483647, 2147483647
                    break
                else:
                    j += 1
            i += 1

        res = 0
        for n in nums:
            if n != 2147483647:
                res = n

        return res
            