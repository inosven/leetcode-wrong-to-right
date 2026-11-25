# LC 84 Largest Rectangle in Histogram
# https://leetcode.com/problems/largest-rectangle-in-histogram/
# 日期: 2026-11-24 | 章节: 单调栈 | 结果: C | 用时: 15min（第 1 版）

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        n = len(heights)
        stack = [0]
        heights.append(0)
        maxArea = 0
        for i in range(n+1):
            while stack and heights[i] < heights[stack[-1]]:
                midpos = stack.pop()
                leftpos = stack[-1]
                rightpos = i
                width = rightpos-leftpos-1
                h = heights[i]
                area = width*h
                maxArea = max(maxArea, area)
            stack.append(i)
        return maxArea
