# LC 151 Reverse Words in a String
# https://leetcode.com/problems/reverse-words-in-a-string/
# 日期: 2026-11-21 | 章节: 字符串 | 结果: B | 用时: 15min

class Solution:
    def reverseWords(self, s: str) -> str:
        def reverse(s):
            left = 0
            right = len(s)-1
            lst = list(s)
            while left <= right:
                lst[left], lst[right] = lst[right], lst[left]
                left+=1
                right-=1
            return lst

        s=s.strip()

        resersed = reverse(s)

        n = len(resersed)
        i = 0
        ans = []
        while i < n:
            if resersed[i] == ' ':
                i+=1
                continue
            elif i ==0 or (i>0 and resersed[i]!=' ' and resersed[i-1]==' '):
                start = i
                while i < n and resersed[i] != ' ':
                    i+=1
                cur = resersed[start:i]
                ans.append(reverse(cur))
                i+=1
        return ' '.join(ans)
