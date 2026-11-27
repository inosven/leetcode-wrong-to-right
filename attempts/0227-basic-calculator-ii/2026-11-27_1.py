# LC 227 Basic Calculator II
# https://leetcode.com/problems/basic-calculator-ii/
# 日期: 2026-11-27 | 章节: 栈与队列 | 结果: B | 用时: 20min

class Solution:
    def calculate(self, s: str) -> int:
        precedence = {"+":1,"-":1,"*":2,"/":2}
        nums = []
        ops = []
        def calstack():
            b = nums.pop()
            a = nums.pop()
            op = ops.pop()
            if op == "+":
                val = a + b
            elif op == "-":
                val = a - b            
            elif op == "*":
                val = a * b            
            elif op == "/":
                val = int(a / b)
            nums.append(val)
            return
        
        s = s.replace(' ','')
        n = len(s)
        i = 0
        while i < n:
            c = s[i]
            if c == '(':
                ops.append(c)
                i+=1
            elif c.isdigit():
                num = int(c)
                while i+1 < n-1 and s[i+1].isdigit():
                    num  = nums*10 + int(s[i+1])
                    i+=1
                nums.append(num)
                i+=1
            elif c == ')':
                while ops[-1]!='(':
                    calstack()
                i+=1
            elif c in precedence:
                if c == '-':
                    if i == 0 or (i>0 and s[i-1] == '('):
                        nums.append(0)
                if precedence[c] <= precedence[ops[-1]]:
                        calstack()
                i+=1
        while ops:
            calstack()
        return nums[-1]
