class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(lambda x: x[0])
        changes = 0
        n = len(intervals)
        i = 0
        while i < n - 1:
            print(intervals[i], intervals[i + 1])
            if (
                intervals[i][0] <= intervals[i + 1][0]
                and intervals[i][1] >= intervals[i + 1][0]
                or intervals[i][0] >= intervals[i + 1][0]
                and intervals[i][0] <= intervals[i + 1][1]
            ):
                intervals[i][0] = min(intervals[i][0], intervals[i + 1][0])
                intervals[i][1] = max(intervals[i][1], intervals[i + 1][1])
                intervals.remove(intervals[i + 1])
                n -= 1
                changes += 1
            i += 1
        if changes:
            return self.merge(intervals)
        return intervals


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
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


# Test Cases
# AABABB
# BBABAA
# ABABAB
# AAABBB
# BBBAAA
# [[0,3],[3,6]]
# [[0,3],[2,5]]
# [[2,5],[0,3]]
# [[0,6],[0,6]]
# [[0,6],[0,6],[0,6]]
