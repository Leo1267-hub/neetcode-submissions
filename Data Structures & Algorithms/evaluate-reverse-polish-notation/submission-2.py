class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            res = token
            if token in '+-*/':
                n1 = stack.pop()
                n2 = stack.pop()
                if token == '+':
                    res = n1 + n2
                elif token == '-':
                    res = n2 - n1
                elif token == '/':
                    res = n2 / n1
                else:
                    res = n1 * n2
            stack.append(int(res))
        return stack[-1]
