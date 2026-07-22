class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        sorted_intervals = sorted(intervals)
        res = []
        curr_start = sorted_intervals[0][0]
        curr_end = sorted_intervals[0][1]

        for i in range(1, len(intervals)):
            if sorted_intervals[i][0] <= curr_end:
                curr_end = max(curr_end, sorted_intervals[i][1])
            else:
                res.append([curr_start, curr_end])
                curr_start = sorted_intervals[i][0]
                curr_end = sorted_intervals[i][1]
        res.append([curr_start, curr_end])

        return res 




