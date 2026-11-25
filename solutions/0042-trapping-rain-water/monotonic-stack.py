# LC 42 Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/
# 单调栈（存下标，高度递减）：弹出坑底 mid，左墙 = 新栈顶，右墙 = i；
# 一层水 = (min(左墙, 右墙) - 坑底) * 宽度；栈空说明没有左墙 → break。O(n) / O(n)

class Solution:
    def trap(self, height: list[int]) -> int:
        water = 0
        stack = []
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                mid = stack.pop()
                if not stack:
                    break
                lefti = stack[-1]

                lefth = height[lefti]
                righti = i
                righth = height[i]
                water += (min(lefth,righth) - height[mid]) * (righti-lefti-1)
            stack.append(i)
        return water
