class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        map = {}
        result = []

        for num in nums:
            map[num] = map.get(num, 0) + 1

        sorted_nums = sorted(map.items(), key=lambda item: item[1], reverse=True)

        result = [num for num, freq in sorted_nums[:k]]

        return result