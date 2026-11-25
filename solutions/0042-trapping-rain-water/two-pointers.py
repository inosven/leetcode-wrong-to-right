# LC 42 Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/
# 双指针：每格水 = min(左边最高, 右边最高) - 自身；哪边矮先结算哪边。O(n) / O(1)

class Solution:
    def trap(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        leftMax = 0
        rightMax = 0
        water = 0
        while left < right:
            if height[left] < height[right]:
                # 右边有更高的墙兜底，左边这一格的水只由 leftMax 决定
                leftMax = max(leftMax, height[left])
                water += leftMax - height[left]
                left += 1
            else:
                rightMax = max(rightMax, height[right])
                water += rightMax - height[right]
                right -= 1
        return water
