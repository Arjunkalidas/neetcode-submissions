class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        if not nums:
            return []

        counts = {}

        for n in nums:
            counts[n] = counts.get(n, 0) + 1

        buckets: List[List[int]] = [[] for _ in range(len(nums) + 1)]
        for n, f in counts.items():
            buckets[f].append(n)

        res = []

        for el in range(len(nums), 0, -1):
            for t in buckets[el]:
                res.append(t)
                if len(res) == k:
                    return res
        return []