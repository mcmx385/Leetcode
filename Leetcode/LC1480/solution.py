import itertools
import numpy as np


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running = [nums[0]]
        for num in nums[1:]:
            running.append(running[-1] + num)
        return running


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return list(itertools.accumulate(nums))


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return np.cumsum(nums).tolist()


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return [sum(nums[: i + 1]) for i in range(len(nums))]
