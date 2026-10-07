class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        sorted_intervals = sorted(intervals)
        n, overlaps = len(intervals), 0
        curr_end = sorted_intervals[0][1]

        for i in range(1, n):
            if sorted_intervals[i][0] >= curr_end:
                curr_end = sorted_intervals[i][1]
            else:
                curr_end = min(curr_end, sorted_intervals[i][1])
                overlaps += 1

        return overlaps