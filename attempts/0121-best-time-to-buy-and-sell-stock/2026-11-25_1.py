# LC 121 Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# 日期: 2026-11-25 | 章节: 动态规划 | 结果: B | 用时: 15min

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # dp[i][0] 第i天不持有股票的最大值
        # dp[i][1] 第i天持有股票的最大值

        n = len(prices)

        dp = [[0] * 2 for _ in range(n)]
        
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1,n):
            dp[i][0] = max(dp[i-1][1]+prices[i] , dp[i-1][0])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])

        return dp[n-1][0]
