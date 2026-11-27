# LC 227 Basic Calculator II
# https://leetcode.com/problems/basic-calculator-ii/
# 单栈（无括号专用）：读完一个数，按它前面的运算符处理：+ 入栈，- 入负数，* / 与栈顶算完放回；最后求和。O(n) / O(n)

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = '+'
        n = len(s)
        for i in range(n):
            c = s[i]
            if c.isdigit():
                num = num * 10 + int(c)
            if (not c.isdigit() and c != ' ') or i == n - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))
                sign = c
                num = 0
        return sum(stack)
