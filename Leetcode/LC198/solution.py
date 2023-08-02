class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(nums[0] + self.rob(nums[2:]), self.rob(nums[1:]))


class Solution:
    def helper(self, start):
        if start >= self.n:
            return 0
        return max(self.helper(start + 1), self.helper(start + 2) + self.nums[start])

    def rob(self, nums: List[int]) -> int:
        self.nums = nums
        self.n = len(nums)
        return self.helper(0)


class Solution:
    def helper(self, start):
        if start >= self.n:
            return 0
        if start in self.dp:
            return self.dp[start]
        self.dp[start] = max(
            self.helper(start + 1), self.helper(start + 2) + self.nums[start]
        )
        return self.dp[start]

    def rob(self, nums: List[int]) -> int:
        self.nums = nums
        self.dp = {}
        self.n = len(nums)
        return self.helper(0)


class Solution:
    def helper(self, start):
        if start >= self.n:
            return 0
        if self.dp[start] != -1:
            return self.dp[start]
        self.dp[start] = max(
            self.helper(start + 1), self.helper(start + 2) + self.nums[start]
        )
        return self.dp[start]

    def rob(self, nums: List[int]) -> int:
        self.nums = nums
        self.dp = [-1] * (len(nums) + 1)
        self.n = len(nums)
        return self.helper(0)


class Solution:
    def rob(self, nums: List[int]) -> int:
        self.dp = [0] * (len(nums) + 1)
        self.dp[1] = nums[0]
        for i in range(2, len(nums) + 1):
            self.dp[i] = max(self.dp[i - 1], self.dp[i - 2] + nums[i - 1])
        return self.dp[-1]


class Solution:
    def rob(self, nums: List[int]) -> int:
        prev = curr = 0
        for num in nums:
            prev, curr = curr, max(prev + num, curr)
        return curr
