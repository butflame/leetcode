from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token.isnumeric() or token.strip("-").isnumeric():
                stack.append(int(token))
            elif token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                op2, op1 = stack.pop(), stack.pop()
                stack.append(int(op1 / op2))
            elif token == "-":
                op2, op1 = stack.pop(), stack.pop()
                stack.append(op1 - op2)
        return stack[-1]
