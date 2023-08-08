class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        best = 0
        n = len(nums)
        if n <= k:
            return sum(nums) / n
        for i in range(n - k + 1):
            avg = sum(nums[i : i + k]) / k
            best = max(best, avg)
        return best


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        if n <= k:
            return sum(nums) / n
        best = currSum = sum(nums[:k])
        for i in range(n - k):
            currSum -= nums[i]
            currSum += nums[i + k]
            best = max(best, currSum)
        return best / k
