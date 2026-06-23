class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        i = 0
        j = len(heights) - 1
        capacity = 0

        while i < j:

            lower = min(heights[i], heights[j])

            capacity = max(capacity, lower * (j - i))

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

        return capacity
