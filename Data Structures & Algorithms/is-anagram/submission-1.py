class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        arr = [0] * 26

        for ch in s:
            idx = ord(ch) - ord('a')
            arr[idx] += 1

        for ch in t:
            idx = ord(ch) - ord('a')
            if arr[idx] == 0:
                arr[idx] += 1
            else:
                arr[idx] -= 1

        return sum(arr) == 0

