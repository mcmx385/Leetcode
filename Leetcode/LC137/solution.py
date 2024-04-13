class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mapp = {}
        for num in nums:
            if num not in mapp:
                mapp[num] = 1
            else:
                mapp[num] += 1
        for num in mapp:
            if mapp[num] == 1:
                return num
        return -1


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mapp = {}
        for num in nums:
            if num not in mapp:
                mapp[num] = False
            else:
                mapp[num] = True
        return [num for num in mapp if not mapp[num]][0]
