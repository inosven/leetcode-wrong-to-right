# LC 121 Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# 贪心：记录到目前为止的最低价，每天用 price - min_price 更新最大利润。O(n) / O(1)

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = prices[0]
        best = 0
        for price in prices:
            if price < min_price:
                min_price = price
            if price - min_price > best:
                best = price - min_price
        return best
