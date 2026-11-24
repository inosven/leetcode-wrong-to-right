# LC 739 Daily Temperatures
# https://leetcode.com/problems/daily-temperatures/
# 日期: 2026-11-24 | 章节: 单调栈 | 结果: A | 用时: 10min

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n=len(temperatures)
        ans = [0] * n

        for i , temperature in enumerate(temperatures):
            while stack and  temperature > temperatures[stack[-1]]:
                ix = stack.pop()
                ans[ix] = i - ix
            stack.append(i)
        return ans
