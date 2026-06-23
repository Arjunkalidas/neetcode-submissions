class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n == 1:
            return 1
        elif n == 2:
            return 2

        arr = [0] * n
        arr[0] = 1
        arr[1] = 2
        i = 2
        
        while i < n:
            arr[i] = arr[i-1] + arr[i-2]
            i += 1

        return arr[n-1]
