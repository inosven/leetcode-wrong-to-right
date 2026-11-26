# LC 121 Best Time to Buy and Sell Stock — 并行版（不是 LeetCode 提交，本地运行：python3 parallel.py）
# 分块 → 每块摘要 (最低价, 最高价, 块内最大利润) → 按顺序合并。ProcessPoolExecutor（GIL 下线程对纯计算不加速）

from concurrent.futures import ProcessPoolExecutor

# (最低价, 最高价, 最大利润)
def merge(left, right):
    leftlow,lefthigh,leftmax = left
    rightlow,righthigh,rightmax = right

    return (min(leftlow,rightlow), max(lefthigh,righthigh), max(rightmax,leftmax,righthigh-leftlow))

def summarize(chunk):
    low = float('inf')
    high = float('-inf')
    maxval = 0
    for p in chunk:
        low= min(low,p)
        high = max(high,p)
        maxval = max(maxval, p-low)
    return (low,high,maxval)

def parallel_max_profit(prices, workers=4):
    workers = min(workers, len(prices))
    n = len(prices)//workers
    chunks = []
    start = 0
    for i in range(workers-1):
        chunks.append(prices[start:start+n])
        start+=n
    chunks.append(prices[start:])

    with ProcessPoolExecutor(max_workers=workers) as executor:
        summaries = list(executor.map(summarize, chunks))

    merged = summaries[0]
    for summary in summaries[1:]:
        merged = merge(merged,summary)
    return merged[2]

if __name__ == "__main__":
    print(parallel_max_profit([3, 8, 1, 5, 2, 9, 4], workers=2))   # 应该输出 8
