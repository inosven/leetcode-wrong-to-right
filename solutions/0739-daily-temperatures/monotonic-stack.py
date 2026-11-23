# LC 739 Daily Temperatures
# https://leetcode.com/problems/daily-temperatures/
# 单调栈存下标（温度递减）；t 弹出栈顶 pos → ans[pos] = i - pos。O(n) / O(n)

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
