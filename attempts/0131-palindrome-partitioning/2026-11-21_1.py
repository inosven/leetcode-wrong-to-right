# LC 131 Palindrome Partitioning
# https://leetcode.com/problems/palindrome-partitioning/
# 日期: 2026-11-21 | 章节: 回溯 | 结果: B | 用时: 15min

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPa(s):
            left = 0
            right = len(s)-1
            while left <= right:
                if s[left] == s[right]:
                    left +=1
                    right-=1
                else:
                    return False
            return True

        path = []
        ans = []
        n = len(s)
        def bt(start):
            if start == n:
                ans.append(path[:])
                return
            for i in range(start,n):
                cur = s[start:i+1]
                if not isPa(cur):
                    continue
                else:
                    path.append(cur)
                    bt(i+1)
                    path.pop()
        bt(0)
        return ans
