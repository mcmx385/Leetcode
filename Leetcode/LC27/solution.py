class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] == val:
                continue
            nums[i] = nums[j]
            i += 1
        return i


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = len(nums)
        while i < j:
            if nums[i] == val:
                nums[i] = nums[j-1]
                j -= 1
            else:
                i += 1
        return i


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = len(nums)
        while i < j:
            if nums[i] == val:
                nums[i] = nums[j-1]
                j -= 1
            else:
                if val in nums:
                    ind = nums.index(val, i+1)
                    i = j if ind >= j else ind
                else:
                    i = j
        return i


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for _ in range(nums.count(val)):
            nums.remove(val)
        return len(nums)


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)
