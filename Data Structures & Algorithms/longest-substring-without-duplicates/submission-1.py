class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        s_set = set()
        longest = 0
        i = 0
        j = 0

        while i < len(s) and j < len(s):
            if s[j] not in s_set:
                s_set.add(s[j])
                longest = max(longest, j - i + 1)
            else:
                while s[i] != s[j] and i < j:
                    s_set.remove(s[i])
                    i += 1
                i += 1
            j += 1
        return longest
            
