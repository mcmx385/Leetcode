class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        result = []
        for num in nums:
            temp = nums.copy()
            temp.remove(num)
            res = self.permuteUnique(temp)
            for i in range(len(res)):
                tempRes = [num] + res[i]
                if tempRes not in result:
                    result.append(tempRes)
        return result


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        result = []
        for num in nums:
            temp = nums.copy()
            temp.remove(num)
            res = self.permuteUnique(temp)
            for i in range(len(res)):
                tempRes = [num] + res[i]
                result.append(tempRes)
        return [list(x) for x in list(set(map(tuple, result)))]


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return set(itertools.permutations(nums))
