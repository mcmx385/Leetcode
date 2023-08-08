class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result=[]
        for num1 in nums1:
            if num1 in nums2 and num1 not in result:
                result.append(num1)
        return result
    

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapp={}
        result=[]
        for num1 in nums1:
            if num1 not in mapp:
                mapp[num1]=1
        for num2 in nums2:
            if num2 in mapp and num2 not in result:
                result.append(num2)
        return result

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapp={}
        result=[]
        for num1 in nums1:
            if num1 not in mapp:
                mapp[num1]=0
        for num2 in nums2:
            if num2 in mapp:
                mapp[num2]=1
        for key in mapp:
            if mapp[key]==1:
                result.append(key)
        return result
    
    
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1=list(set(nums1))
        nums2=list(set(nums2))
        result=[]
        for num1 in nums1:
            if num1 in nums2:
                result.append(num1)
        return result

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(nums1) & set(nums2)

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        x=set(nums1)
        y=set(nums2)
        return list(x.intersection(y))


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1=set(nums1)
        result=[]
        for num2 in nums2:
            if num2 in nums1:
                result.append(num2)
        return result
    

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1=set(nums1)
        nums2=set(nums2)
        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1
        result=[]
        for num1 in nums1:
            if num1 in nums2:
                result.append(num1)
        return result