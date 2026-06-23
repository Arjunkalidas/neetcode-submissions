class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        stack = []
        max_profit = 0

        for n in prices:
            if stack:
                if n <= stack[-1]:
                    stack.pop()
                    stack.append(n)
                else:
                    max_profit = max(max_profit, n - stack[-1])
            else:
                stack.append(n)
        
        return max_profit