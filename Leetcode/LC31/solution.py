class Solution:
    # [4,3,2,1] -> [1,2,3,4]
    # [1,2,3,4] -> [2,1,3,4]
    # [2,1,3,4] -> [2,3,1,4]
    def helper(self, nums, pos):
        if pos == len(nums) - 1:
            return False
        if self.helper(nums, pos + 1):
            return True
        else:
            arr = sorted(nums[pos:], reverse=True)
            if nums[pos] == min(nums):
                nums = arr
                return True
            ind = arr.index(nums[pos])
            temp = nums[pos]
            nums[pos] = nums[pos + 1]
            nums[pos + 1] = temp
            arr.remove(nums[pos])
            j = 0
            for i in range(pos + 1, len(nums)):
                nums[i] = arr[j]
                j += 1
            return True

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        desc = True
        for i in range(1, len(nums)):
            print(nums[i], nums[i - 1])
            if nums[i] > nums[i - 1]:
                desc = False
        print(desc)
        if desc:
            nums = sorted(nums)
            print(nums)
            return
        return self.helper(nums, 0)


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = len(nums) - 2
        while left >= 0 and nums[left] >= nums[left + 1]:
            left -= 1
        if left == -1:
            nums.sort()
            return
        right = len(nums) - 1
        while right >= 0 and nums[right] <= nums[left]:
            right -= 1
        nums[left], nums[right] = nums[right], nums[left]
        nums[left + 1 :] = nums[left + 1 :][::-1]
        return
