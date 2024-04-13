# does not pass all test cases
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        nums = [0] + nums
        start = 0
        end = len(nums) - 1
        leftSum = nums[start]
        rightSum = nums[end]
        start += 1
        end -= 1
        while start <= end:
            print(start, end, nums[start], nums[end], leftSum, rightSum)
            if leftSum == rightSum and start == end:
                return start - 1
            if leftSum >= rightSum:
                rightSum += nums[end]
                end -= 1
            else:
                leftSum += nums[start]
                start += 1
        return -1


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = 0
        rightSum = sum(nums)
        for ind, num in enumerate(nums):
            rightSum -= num
            if leftSum == rightSum:
                return ind
            leftSum += num
        return -1
