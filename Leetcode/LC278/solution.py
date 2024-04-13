# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersion(self, n: int) -> int:
        for i in range(1, n + 1):
            if isBadVersion(i):
                return i
        return -1


class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n
        while start < end:
            mid = (start + end) // 2
            if not isBadVersion(mid - 1) and isBadVersion(mid):
                return mid
            elif isBadVersion(mid - 1) and isBadVersion(mid):
                end = mid
            else:
                start = mid + 1
        return start
