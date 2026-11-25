# LC 42 Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/
# 日期: 2026-11-24 | 章节: 单调栈 | 结果: B | 用时: 20min

class Solution:
    def trap(self, height: list[int]) -> int:
        water = 0
        stack = []
        for i in range(len(height)):
            while stack and height[i] > stack[-1]:
                mid = stack.pop()
                lefti = stack[-1] if stack else i-1

                lefth = height[lefti]
                righti = i
                righth = height[i]
                water += min(lefth,righth) * (righti-lefti-1)
            stack.append(i)
        return water
