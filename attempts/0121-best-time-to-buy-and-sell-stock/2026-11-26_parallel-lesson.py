# LC 121 并行版（讲解，第一次，不计成绩）
# 日期: 2026-11-26 | 章节: 动态规划 | 结果: 讲解

from concurrent.futures import ProcessPoolExecutor

class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        # (最低价, 最高价, 最大利润)
        def merge(left, right):
            leftlow,lefthigh,leftmax = left
            rightlow,righthigh,rightmax = right
            
            return (min(leftlow,rightlow), max(lefthigh,righthigh), max(rightmax,leftmax,righthigh-leftlow))

        def summarize(chunk):
            low = float('inf')
            high = 0
            maxval = 0
            for p in chunk:
                low= min(low,p)
                high = max(high,p)
                maxval = max(maxval, high-low)
            return (low,high,maxval)

        def parallel_max_profit(prices, workers=4):
            if len(prices) >= workers:
                res = len(prices) % workers
                n = len(prices)//workers
                chunks = []
                start = 0
                for i in range(wokers-1):
                    chunks.append(prices[start:start+n])
                    start+=n
                chunks.append(prices[start:start+res])
                summaries = []
                for chunk in chunks:
                    summaries.append(summarize(chunk))
                for summary in summaries:
                    merged = merge(merged,summary)
            return (low,high,maxval)
if __name__ == "__main__":
    print(parallel_max_profit([3, 8, 1, 5, 2, 9, 4], workers=2))   # 应该输出 8
