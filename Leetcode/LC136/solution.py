import numpy as np


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        obj = {}
        for num in nums:
            if num not in obj:
                obj[num] = 1
            else:
                obj[num] += 1
        obj = {val: key for key, val in obj.items()}
        return obj[1]


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        obj = {}
        for num in nums:
            if num not in obj:
                obj[num] = 1
            else:
                obj[num] += 1
        obj = sorted(obj.items(), key=lambda x: x[1])
        return obj[0][0]


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        obj = {}
        for num in nums:
            if num not in obj:
                obj[num] = 1
            else:
                obj[num] += 1
        for key, val in obj.items():
            if val == 1:
                return key


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        occurences = np.bincount(nums)
        return np.where(occurences == 1)[0][0]


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums.count(nums[i]) == 1:
                return nums[i]


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums not in nums[:i] + nums[i+1:]:
                return nums[i]


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(0, len(nums)-1, 2):
            if nums[i] != nums[i+1]:
                return nums[i]


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        candidate = nums[0]
        for num in nums[1:]:
            candidate ^= num
        return candidate


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)-1):  # time complexity: O(n), space complexity: O(1)
            nums[i+1] ^= nums[i]
        return nums[-1]
