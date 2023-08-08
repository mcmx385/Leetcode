class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapp={}
        result=[]
        for num1 in nums1:
            if num1 not in mapp:
                mapp[num1]=0
            mapp[num1]+=1
        for num2 in nums2:
            if num2 in mapp and mapp[num2]>0:
                result.append(num2)
                mapp[num2]-=1
        return result