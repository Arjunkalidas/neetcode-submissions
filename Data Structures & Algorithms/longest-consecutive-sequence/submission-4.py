class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        unique_nums = set(nums)
        maxlen = 0

        for num in unique_nums:
            if (num - 1) not in unique_nums:
                arr = []
                arr.append(num)
                while (num + 1) in unique_nums:
                    arr.append(num + 1)
                    num += 1
                maxlen = max(maxlen, len(arr))

        return maxlen