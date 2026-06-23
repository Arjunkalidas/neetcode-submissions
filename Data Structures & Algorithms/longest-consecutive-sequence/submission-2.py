class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        unique_nums = set(nums)
        maxlen = 0

        for i, num in enumerate(nums):
            if num - 1 not in unique_nums:
                arr = []
                arr.append(num)
                while num + 1 in unique_nums:
                    arr.append(num + 1)
                    num += 1
                maxlen = max(maxlen, len(arr))
            i += 1
        return maxlen