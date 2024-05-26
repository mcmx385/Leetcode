class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        total = len(nums)
        if total <= 1:
            return total
        count = Counter(nums)

        i = 0
        for key in count:
            times = 2 if count[key] >= 2 else count[key]
            for times in range(times):
                nums[i] = key
                i += 1
        return i


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        total = len(nums)
        if total <= 1:
            return total
        count = {}
        for num in nums:
            if num in count:
                if count[num] < 2:
                    count[num] += 1
            else:
                count[num] = 1

        i = 0
        for key in count:
            for times in range(count[key]):
                nums[i] = key
                i += 1
        return i


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        total = len(nums)
        if total <= 1:
            return total
        currIndex = 1
        uniqueItems = 1
        prevValue = nums[0]
        appearedTimes = 1
        for i in range(1, total):
            if nums[i] == prevValue:
                print("same value")
                appearedTimes += 1
                if appearedTimes <= 2:
                    if i != currIndex:
                        nums[currIndex] = nums[i]
                    uniqueItems += 1
                    currIndex += 1
            else:
                if i != currIndex:
                    nums[currIndex] = nums[i]
                appearedTimes = 1
                uniqueItems += 1
                currIndex += 1
            prevValue = nums[i]
        return uniqueItems
