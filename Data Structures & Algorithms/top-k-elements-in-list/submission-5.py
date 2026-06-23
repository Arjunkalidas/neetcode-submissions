class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        map: dict[int, int] = defaultdict(int)
        result = []

        for num in nums:
            map[num] += 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for n, f in map.items():
            buckets[f].append(n)

        for f in range(len(nums), 0, -1):
            for n in buckets[f]:
                result.append(n)
                if len(result) == k:
                    return result

        return result