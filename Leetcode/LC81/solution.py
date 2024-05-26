class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        temp_nums = sorted(nums)
        indices = sorted(range(len(nums)), key=lambda k: nums[k])
        start = 0
        end = len(temp_nums) - 1
        mid = start + (end - start) // 2
        while start <= end:
            mid = start + (end - start) // 2
            if temp_nums[mid] == target:
                return True
            elif temp_nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return False


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        return target in nums
