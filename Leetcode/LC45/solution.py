from typing import List
from functools import lru_cache


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float("inf") for _ in range(n)]
        dp[0] = 0
        for i in range(n):
            for j in range(1, nums[i] + 1):
                if i + j < n:
                    dp[i + j] = min(dp[i + j], dp[i] + 1)
        return dp[n - 1]


class Solution:
    def helper(self, i):
        if i >= len(self.nums) - 1:
            return 0
        if i in self.dictt:
            return self.dictt[i]
        res = float("inf")
        for j in range(1, self.nums[i] + 1):
            res = min(res, self.helper(i + j) + 1)
        self.dictt[i] = res
        return res

    def jump(self, nums: List[int]) -> int:
        self.nums = nums
        self.dictt = {}
        return self.helper(0)


class Solution:
    @lru_cache(None)
    def helper(self, i):
        if i >= len(self.nums) - 1:
            return 0
        res = float("inf")
        for j in range(1, self.nums[i] + 1):
            res = min(res, self.helper(i + j) + 1)
        return res

    def jump(self, nums: List[int]) -> int:
        self.nums = nums
        return self.helper(0)


class Solution:
    def helper(self, nums, start):
        if start >= len(nums) - 1:
            return 0
        if nums[start] <= 0:
            return float("inf")
        once = self.helper(nums, start + 1)
        for i in range(start + 1, start + nums[start] + 1):
            once = min(once, self.helper(nums, i))
        return 1 + once

    def jump(self, nums: List[int]) -> int:
        return self.helper(nums, 0)


class Solution:
    def helper(self, nums, start):
        if start >= self.n - 1:
            return 0
        elif nums[start] <= 0:
            return float("inf")
        step = self.getStep(start + 1)
        if step == 0:
            once = self.helper(nums, start + 1)
            self.storeStep(start + 1, once)
        else:
            once = step
        for i in range(start + 1, start + nums[start] + 1):
            step = self.getStep(i)
            if step == 0:
                num = self.helper(nums, i)
                self.storeStep(i, num)
            else:
                num = step
            once = min(once, num)
        return 1 + once

    def getStep(self, step):
        if step >= self.n - 1:
            return 0
        return self.steps[step]

    def storeStep(self, step, val):
        if step < self.n:
            self.steps[step] = val

    def jump(self, nums: List[int]) -> int:
        self.n = len(nums)
        self.steps = [0 for _ in range(self.n)]
        return self.helper(nums, 0)


solution = Solution()
nums = [3, 2, 1]
nums = [4, 1, 1, 3, 1, 1, 1]
print(solution.jump(nums))
