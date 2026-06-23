class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        i = 0
        curr_sum = 0
        max_sum = nums[0]

        while i < len(nums):

            curr_sum = max(curr_sum + nums[i], nums[i])

            max_sum = max(max_sum, curr_sum)

            i += 1

        return max_sum