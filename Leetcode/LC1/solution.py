class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if target - nums[i] == nums[j]:
                    return [i, j]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_key = [(num, i) for i, num in enumerate(nums)]
        num_key.sort()
        i = 0
        j = len(nums) - 1
        while i < j:
            total = num_key[i][0] + num_key[j][0]
            if total == target:
                return [num_key[i][1], num_key[j][1]]
            elif total < target:
                i += 1
            else:
                j -= 1
