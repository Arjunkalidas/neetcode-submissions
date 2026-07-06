class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        prev_min, prev_max, global_max = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            n = nums[i]
            temp_min = prev_min
            temp_max = prev_max

            prev_min = min(n, temp_min * n, temp_max * n)
            prev_max = max(n, temp_min * n, temp_max * n)

            global_max = max(global_max, prev_max)

        return global_max