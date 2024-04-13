class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums) - 1
        result = [-1, -1]
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                result = [mid, mid]
                for i in range(mid - 1, -1, -1):
                    if nums[i] == target:
                        result[0] = i
                    else:
                        break
                for i in range(mid + 1, len(nums)):
                    if nums[i] == target:
                        result[1] = i
                    else:
                        break
                return result
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return result


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.biasedBinSearch(nums, target, True)
        right = self.biasedBinSearch(nums, target, False)
        return [left, right]

    def biasedBinSearch(self, nums, target, leftBias):
        start = 0
        end = len(nums) - 1
        i = -1
        while start <= end:
            mid = (start + end) // 2
            print(mid)
            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                i = mid
                if leftBias:
                    end = mid - 1
                else:
                    start = mid + 1
        return i
