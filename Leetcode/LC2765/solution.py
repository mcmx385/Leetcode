class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        small = large = -1
        longest = -1
        count = -1
        started = False
        left = True
        for i in range(1, len(nums)):
            num = nums[i]
            prev = nums[i - 1]
            print(num, prev, started, left, count, small, large)
            if not started:
                if num - prev == 1:
                    started = True
                    left = False
                    count = 2
                    small = prev
                    large = num
            else:
                if left:
                    if num == large:
                        count += 1
                        left = False
                    else:
                        left = True
                        longest = max(longest, count)
                        count = -1
                        started = False
                        if num - prev == 1:
                            started = True
                            left = False
                            count = 2
                            small = prev
                            large = num
                else:
                    if num == small:
                        count += 1
                        left = True
                    else:
                        left = True
                        longest = max(longest, count)
                        count = -1
                        started = False
                        if num - prev == 1:
                            started = True
                            left = False
                            count = 2
                            small = prev
                            large = num
        return max(longest, count)


class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        res = -1
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] == 1:
                longest = 2
                for j in range(i + 2, len(nums)):
                    if j < len(nums) and nums[j] == nums[j - 2]:
                        longest += 1
                    else:
                        break
                res = max(res, longest)
        return res if res != 0 else -1
