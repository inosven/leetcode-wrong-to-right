# LC 739 Daily Temperatures
# https://leetcode.com/problems/daily-temperatures/
# 日期: 2026-11-21 | 章节: 单调栈 | 结果: A | 用时: 5min

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        ans = [0] * n
        for i,t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                pos = stack.pop()
                ans[pos] = i-pos
            stack.append(i)
        return ans
