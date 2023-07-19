class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0] * 3
        for num in nums:
            count[num] += 1
        ind = 0
        for i in range(3):
            nums[ind : ind + count[i]] = [i] * count[i]
            ind += count[i]


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0] * 3
        for num in nums:
            count[num] += 1
        ind = 0
        for i in range(3):
            for j in range(count[i]):
                nums[ind] = i
                ind += 1


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ind = 0
        for i in range(3):
            for j in range(ind, len(nums)):
                if nums[j] == i:
                    nums[ind], nums[j] = nums[j], nums[ind]
                    ind += 1


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroEnd = 0
        twoStart = len(nums) - 1
        i = 0
        while i <= twoStart:
            if nums[i] == 0:
                nums[i], nums[zeroEnd] = nums[zeroEnd], nums[i]
                zeroEnd += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[twoStart] = nums[twoStart], nums[i]
                twoStart -= 1
            else:
                i += 1
