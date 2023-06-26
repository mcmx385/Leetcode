class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxArea = 0
        while left < right:
            currHeight = min(height[left], height[right])
            currWidth = right - left
            currArea = currWidth * currHeight
            maxArea = max(currArea, maxArea)
            if height[left] > height[right]:
                right -= 1
            elif height[right] > height[left]:
                left += 1
            else:
                left += 1
                right -= 1
        return maxArea
