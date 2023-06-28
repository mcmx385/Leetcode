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
    def helper(self, start):
        print(start)
        if start == self.n - 1:
            return 0
        elif start > self.n - 1:
            return float("inf")
        print("going to", start + 1, start + self.nums[start])
        if start + 1 < self.n:
            once = self.helper(start + 1) + 1
            print("got once", once)
        else:
            once = float("inf")
        if start + self.nums[start] < self.n:
            num = self.helper(start + self.nums[start]) + 1
            print("got num", num)
        else:
            num = float("inf")
        return min(once, num)

    def jump(self, nums: List[int]) -> int:
        self.nums = nums
        self.n = len(nums)
        return self.helper(0)


class Solution:
    def helper(self, nums, start):
        print(nums, start, self.steps)
        if start >= len(nums) - 1:
            print("reached end")
            return 0
        if self.steps[start + 1] == 0:
            once = self.helper(nums, start + 1)
            self.steps[start + 1] = once
        else:
            once = self.steps[start + 1]
        if self.steps[start + nums[start]] == 0:
            num = self.helper(nums, start + nums[start])
            self.steps[start + nums[start]] = num
        else:
            num = self.steps[start + nums[start]]
        return 1 + min(once, num)

    def jump(self, nums: List[int]) -> int:
        self.steps = [0 for _ in range(len(nums))]
        return self.helper(nums, 0)
