# LC 84 Largest Rectangle in Histogram
# https://leetcode.com/problems/largest-rectangle-in-histogram/
# 单调栈（存下标，高度递增）+ 两头 0 哨兵：弹出 midpos 以它为高，左边界 = 新栈顶，右边界 = i。O(n) / O(n)

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        n = len(heights)
        stack = [0]
        heights.insert(0,0)
        heights.append(0)
        maxArea = 0
        for i in range(1,n+2):
            while stack and heights[i] < heights[stack[-1]]:
                midpos = stack.pop()
                leftpos = stack[-1]
                rightpos = i
                width = rightpos-leftpos-1
                h = heights[midpos]
                area = width*h
                maxArea = max(maxArea, area)
            stack.append(i)
        return maxArea
