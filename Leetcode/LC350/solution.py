class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapp = {}
        result = []
        for num1 in nums1:
            if num1 not in mapp:
                mapp[num1] = 0
            mapp[num1] += 1
        for num2 in nums2:
            if num2 in mapp and mapp[num2] > 0:
                result.append(num2)
                mapp[num2] -= 1
        return result


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i = 0
        j = 0
        result = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return result


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i = 0
        j = 0
        result = {}
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                if nums1[i] not in result:
                    result[nums1[i]] = 0
                result[nums1[i]] += 1
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        result = list(result.items())
        return [x[0] for x in result for i in range(x[1])]


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        mapp1 = {}
        mapp2 = {}
        for num1 in nums1:
            if num1 not in mapp1:
                mapp1[num1] = 0
            mapp1[num1] += 1
        for num2 in nums2:
            if num2 not in mapp2:
                mapp2[num2] = 0
            mapp2[num2] += 1
        result = []
        for key in mapp1:
            if key in mapp2:
                result.extend([key] * min(mapp1[key], mapp2[key]))
        return result


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        mapp1 = {}
        mapp2 = {}
        for num1 in nums1:
            if num1 not in mapp1:
                mapp1[num1] = 0
            mapp1[num1] += 1
        for num2 in nums2:
            if num2 not in mapp2:
                mapp2[num2] = 0
            mapp2[num2] += 1
        result = []
        i = 0
        j = 0
        mapp1_keys = list(mapp1.keys())
        mappp2_keys = list(mapp2.keys())
        while i < len(mapp1) and j < len(mapp2):
            if mapp1_keys[i] == mappp2_keys[j]:
                result.extend(
                    [mapp1_keys[i]] * min(mapp1[mapp1_keys[i]], mapp2[mappp2_keys[j]])
                )
                i += 1
                j += 1
            elif mapp1_keys[i] < mappp2_keys[j]:
                i += 1
            else:
                j += 1
        return result
