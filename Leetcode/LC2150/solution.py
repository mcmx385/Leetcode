class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        nums.sort()
        lonely = set()
        if nums[1] - nums[0] > 1:
            lonely.add(nums[0])
        for i in range(1, len(nums) - 1):
            if nums[i] - nums[i - 1] > 1 and nums[i + 1] - nums[i] > 1:
                lonely.add(nums[i])
        if nums[-1] - nums[-2] > 1:
            lonely.add(nums[-1])
        return list(lonely)
