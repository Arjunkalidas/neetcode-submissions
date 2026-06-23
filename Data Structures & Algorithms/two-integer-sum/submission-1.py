class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        mapping = {}

        for i, val in enumerate(nums):
            diff = target - val
            if diff not in mapping:
                mapping[val] = i
            elif diff in mapping:
                result.append(mapping[diff])
                result.append(i)
                return result