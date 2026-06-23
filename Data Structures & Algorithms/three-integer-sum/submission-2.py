class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        i = 0

        nums = sorted(nums)
        result = []

        while i < len(nums) - 2:
            j = i + 1
            k = len(nums) - 1
            target = -1 * nums[i]

            while j < k:
                if nums[j] + nums[k] < target:
                    j += 1
                elif nums[j] + nums[k] > target:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    k -= 1
                    while k > j and nums[k] == nums[k+1]:
                        k -= 1

            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1


        return result

