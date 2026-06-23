class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        map = {}
        result = []

        for num in nums:
            map[num] = map.get(num, 0) + 1

        sorted_nums = sorted(map.items(), key=lambda item: item[1], reverse=True)

        for i in sorted_nums:
            if k <= 0:
                break
            else:
                result.append(i[0])
                k -= 1

        return result