class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        occurrences = defaultdict(list)

        for s in strs:
            arr = [0] * 26
            for ch in s:
                arr[ord(ch) - ord('a')] += 1
            occurrences[tuple(arr)].append(s)

        return list(occurrences.values())