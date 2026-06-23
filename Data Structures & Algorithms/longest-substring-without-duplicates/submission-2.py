class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        unique = set()
        max_len = 0
        i = j = 0

        while i < len(s) and j < len(s):

            if s[j] not in unique:
                unique.add(s[j])
                max_len = max(max_len, j - i + 1)
            else:
                while s[i] != s[j] and i < j:
                    unique.remove(s[i])
                    i += 1
                i += 1
            j += 1
        return max_len
        


