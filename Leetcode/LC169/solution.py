import numpy as np


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        for num in count:
            if count[num] > len(nums) / 2:
                return num


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        return max(count, key=count.get)


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = np.bincount(nums)
        return np.argmax(count)


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums) // 2]


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return Counter(nums).most_common(1)[0][0]


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for num in set(nums):
            if nums.count(num) > len(nums) // 2:
                return num