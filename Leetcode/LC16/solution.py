import sys
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closestSum = 0
        closestDiff = sys.maxsize
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                currSum = nums[i] + nums[j] + nums[k]
                if currSum == target:
                    return target
                currDiff = abs(target - currSum)
                if currDiff < closestDiff:
                    closestDiff = currDiff
                    closestSum = currSum
                if currSum < target:
                    j += 1
                else:
                    k -= 1
        return closestSum
