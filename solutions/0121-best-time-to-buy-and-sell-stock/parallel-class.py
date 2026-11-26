# LC 121 并行版 — 写进 class Solution 的形式（本地运行：python3 parallel-class.py）
# 交给进程池的函数用 @staticmethod，以 Solution.summarize 传入（能按名字 pickle）；嵌套在方法里的函数不能 pickle

from concurrent.futures import ProcessPoolExecutor

class Solution:
    @staticmethod
    def summarize(chunk):
        low = float('inf')
        high = float('-inf')
        maxval = 0
        for p in chunk:
            low = min(low, p)
            high = max(high, p)
            maxval = max(maxval, p - low)
        return (low, high, maxval)

    @staticmethod
    def merge(left, right):
        leftlow, lefthigh, leftmax = left
        rightlow, righthigh, rightmax = right
        return (min(leftlow, rightlow), max(lefthigh, righthigh), max(rightmax, leftmax, righthigh - leftlow))

    def maxProfit(self, prices: list[int], workers: int = 4) -> int:
        workers = min(workers, len(prices))
        n = len(prices) // workers
        chunks = []
        start = 0
        for i in range(workers - 1):
            chunks.append(prices[start:start + n])
            start += n
        chunks.append(prices[start:])

        with ProcessPoolExecutor(max_workers=workers) as executor:
            summaries = list(executor.map(Solution.summarize, chunks))

        merged = summaries[0]
        for summary in summaries[1:]:
            merged = Solution.merge(merged, summary)
        return merged[2]

if __name__ == "__main__":
    print(Solution().maxProfit([3, 8, 1, 5, 2, 9, 4], workers=2))
