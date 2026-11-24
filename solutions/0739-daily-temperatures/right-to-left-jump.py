# LC 739 Daily Temperatures
# https://leetcode.com/problems/daily-temperatures/
# 从右往左 + 用 ans 跳跃：j 不够暖就跳到 j + ans[j]；ans[j] == 0 说明后面没有更暖的。均摊 O(n) / O(1) 额外空间

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n

        for i in range(n - 2, -1, -1):          # 最后一天答案一定是 0，从倒数第二天开始
            j = i + 1
            while temperatures[j] <= temperatures[i]:
                if ans[j] == 0:                 # j 之后没有比 j 更暖的，也就不会有比 i 更暖的
                    j = -1
                    break
                j = j + ans[j]                  # 跳到比 j 更暖的那一天
            if j != -1:
                ans[i] = j - i
        return ans
