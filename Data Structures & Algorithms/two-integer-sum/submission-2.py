class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        result = []
        counts = {}

        for i, n in enumerate(nums):
            if target - n in counts:
                result.append(counts.get(target - n))
                result.append(i)
            else:
                counts[n] = i


        return result