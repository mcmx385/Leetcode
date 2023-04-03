import collections
import numpy as np


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for num in nums:
            if nums.count(num) > 1:
                return True
        return False


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for num in nums:
            if num in nums[nums.index(num)+1:]:
                return True
        return False


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(np.unique(nums))


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(collections.Counter(nums))


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for num in nums:
            if num in hashmap:
                return True
            else:
                hashmap[num] = 1
        return False