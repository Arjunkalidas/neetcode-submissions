class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        words = {}

        for word in strs:
            sublist = []
            key = ''.join(sorted(word))
            if key in words:
                words[key].append(word)
            else:
                sublist.append(word)
                words[key] = sublist

        return list(words.values())
