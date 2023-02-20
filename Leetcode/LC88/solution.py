from functools import reduce


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[m:] = nums2
        nums1.sort()


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1 = reduce(lambda x, y: x+y, [nums1, nums2])


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[m:] = nums2
        nums1 = sorted(nums1)


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums3 = nums1[:m].copy()
        i = j = k = 0
        while i < m or j < n:
            if i < m and j < n:
                if nums3[i] < nums2[j]:
                    nums1[k] = nums3[i]
                    i += 1
                else:
                    nums1[k] = nums2[j]
                    j += 1
                k += 1
                continue
            if i < m:
                nums1[k] = nums3[i]
                i += 1
            if j < n:
                nums1[k] = nums2[j]
                j += 1
            k += 1


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        k = m+n-1
        i = m-1
        j = n-1
        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
            continue
        while i >= 0:
            nums1[k] = nums1[i]
            i -= 1
            k -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
