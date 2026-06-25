class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0

        while i < (len(intervals)) and newInterval[0] > intervals[i][1]:
            result.append(intervals[i])
            i += 1

        while i < (len(intervals)) and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        result.append(newInterval)

        while i < (len(intervals)):
            result.append(intervals[i])
            i += 1

        return result