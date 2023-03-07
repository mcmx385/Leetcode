class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        leftOnes = 0
        rightOnes = 0
        mostOnes = 0
        haveZero = False
        for num in nums:
            if num==0:
                haveZero=True
                break
        for num in nums:
            if num == 0:
                if (leftOnes+rightOnes) > mostOnes:
                    mostOnes = leftOnes+rightOnes
                leftOnes = rightOnes
                rightOnes = 0
            else:
                rightOnes += 1
        if nums[-1] != 0:
            if (leftOnes+rightOnes) > mostOnes:
                mostOnes = leftOnes+rightOnes
        if not haveZero:
            mostOnes -= 1
        return mostOnes