class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        mid = end - start // 2
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] <= nums[end]:
                if nums[mid] <= target and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                if nums[start] <= target and target <= nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
        return -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        temp_nums = sorted(nums)
        indices = sorted(range(len(nums)), key=lambda k: nums[k])
        start = 0
        end = len(temp_nums) - 1
        mid = start + (end - start) // 2
        while start <= end:
            mid = start + (end - start) // 2
            if temp_nums[mid] == target:
                return indices[mid]
            elif temp_nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1
