class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = 0
        left, right = 0, len(nums) - 1
        mod = 10**9 + 7
        while left <= right:
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                result += pow(2, right - left, mod)
                left += 1
        return result % mod
