class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        result = []
        for num in nums:
            temp = nums.copy()
            temp.remove(num)
            res = self.permute(temp)
            for i in range(len(res)):
                res[i] = [num]+res[i]
            result += res
        return result


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        result = [num for num in nums]
        for i in range(len(nums)-1):
            temp = []
            for num in nums:
                temp += [[num]+res for res in result if num not in res]
            result = temp
        return result
