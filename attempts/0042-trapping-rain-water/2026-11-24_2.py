# LC 42 Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/
# 日期: 2026-11-24 | 章节: 单调栈 | 结果: C | 用时: 15min（双指针）

class Solution:
    def trap(self, height: list[int]) -> int:
        water = 0
        n=len(height)
        left = 0
        right = n-1
        left_max = 0
        right_max = 0

        while left <= right:
            if left_max<=right_max:
                if left_max-height[left] >=0:
                    water += left_max-height[left]
                left_max = max(left_max,height[left])
                left+=1
            else:
                if right_max-height[right] >=0:
                    water += right_max-height[right]
                right_max = max(right_max,height[right])
                right-=1
        return water
