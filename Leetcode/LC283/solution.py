class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        total=len(nums)
        count=0
        for j in range(total):
            if nums[j]!=0:
                nums[i]=nums[j]
                i+=1
            else:
                count+=1
        for k in range(total-count,total):
            nums[k]=0