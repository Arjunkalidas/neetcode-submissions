class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pre = 1
        post = 1

        res = [1] * len(nums)
        i = 0

        while i < len(nums):
            res[i] = pre
            pre *= nums[i]
            i += 1

        i = len(nums) - 1
        while i >= 0:
            res[i] *= post
            post *= nums[i]
            i -= 1
        return res