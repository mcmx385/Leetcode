class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return len([x for x in nums if x < target])


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)
        mid = (start+end)//2
        if target > nums[end-1]:
            return end
        if target < nums[start]:
            return start
        while start < end:
            if nums[mid] == target:
                while mid > 0 and nums[mid-1] == target:
                    mid -= 1
                return mid
            elif nums[mid] > target:
                end = mid
            else:
                start = mid+1
            mid = (start+end)//2
        return mid


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)


class Solution:
    def search_insert(self, nums, target, start, end):
        if start == end:
            return start
        mid = (start+end)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.search_insert(nums, target, start, mid)
        else:
            return self.search_insert(nums, target, mid+1, end)

    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.search_insert(nums, target, 0, len(nums))


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums, target)
