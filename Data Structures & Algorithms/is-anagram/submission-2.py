class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        position_arr = [0] * 26
        for ch in s:
            position_arr[ord(ch) - ord('a')] += 1

        for ch in t:
            if position_arr[ord(ch) - ord('a')] > 0:
                position_arr[ord(ch) - ord('a')] -= 1
            else:
                position_arr[ord(ch) - ord('a')] += 1

        return sum(position_arr) == 0
