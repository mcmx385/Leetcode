class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        n = len(intervals)
        i = 0
        while i < n - 1:
            if (
                intervals[i][0] <= intervals[i + 1][0]
                and intervals[i][1] >= intervals[i + 1][0]
            ):
                intervals[i][1] = max(intervals[i][1], intervals[i + 1][1])
                intervals.remove(intervals[i + 1])
                n -= 1
                continue  # repeat this i after removing the next interval
            i += 1
        return intervals
    
class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        for i in range(len(intervals)):
            if intervals[i][0] > newInterval[0]:
                intervals.insert(i, newInterval)
                break
        n = len(intervals)
        i = 0
        while i < n - 1:
            if (
                intervals[i][0] <= intervals[i + 1][0]
                and intervals[i][1] >= intervals[i + 1][0]
            ):
                intervals[i][1] = max(intervals[i][1], intervals[i + 1][1])
                intervals.remove(intervals[i + 1])
                n -= 1
                continue  # repeat this i after removing the next interval
            i += 1
        return intervals
