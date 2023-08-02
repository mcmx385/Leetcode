from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            temp = nums[i : i + k + 1]
            if len(set(temp)) != len(temp):
                return True
        return False


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mapp = {}
        for i, num in enumerate(nums):
            if num in mapp and i - mapp[num] <= k:
                return True
            mapp[num] = i
        return False
