class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        words = defaultdict(list)

        for word in strs:
            counts = [0] * 26
            
            for ch in word:
                counts[ord(ch) - ord('a')] += 1
            
            words[tuple(counts)].append(word)

        return list(words.values())
