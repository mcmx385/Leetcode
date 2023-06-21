class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = 0
        for length in range(1, len(nums) + 1):
            print(length)
            for i in range(len(nums) - length + 1):
                print(
                    i,
                    i + length - 1,
                    nums[i],
                    nums[i + length - 1],
                    nums[i] + nums[i + length - 1],
                )
                if (nums[i] + nums[i + length - 1]) <= target:
                    print(nums[i : i + length])
                    if length > 2:
                        tempLength = length
                        while tempLength > 2:
                            result += tempLength - 2
                            tempLength -= 1
                        result += 1
                    else:
                        result += 1
                else:
                    break
        return result
