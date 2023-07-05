# keep going see where it can reach farthest
# consecutive 0s then cannot

class Solution:
    def helper(self, nums, start):
        if start == self.n - 1:
            return True
        elif start > self.n - 1:
            return False
        if nums[start] <= 0:
            return False
        once = self.helper(nums, start + 1)
        for i in range(start + 1, start + nums[start] + 1):
            once = once or self.helper(nums, i)
        return once

    def canJump(self, nums: List[int]) -> bool:
        self.n = len(nums)
        return self.helper(nums, 0)


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        n = len(nums)
        for i in range(n):
            farthest = max(farthest, i + nums[i])
            if nums[i] == 0 and i < n - 1 and i == farthest:
                return False
        return True
