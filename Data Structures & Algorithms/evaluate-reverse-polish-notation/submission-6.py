class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        i = 0

        while i < len(tokens):
            if tokens[i] not in ["+", "-", "*", "/"]:
                stack.append(tokens[i])
            
            if tokens[i] == "+":
                b = int(stack.pop())
                a = int(stack.pop())
                res = a+b
                stack.append(res)

            elif tokens[i] == "-":
                b = int(stack.pop())
                a = int(stack.pop())
                res = a-b
                stack.append(res)

            elif tokens[i] == "*":
                b = int(stack.pop())
                a = int(stack.pop())
                res = a*b
                stack.append(res)

            elif tokens[i] == "/":
                b = int(stack.pop())
                a = int(stack.pop())
                res = a/b
                stack.append(res)
            i+=1

        return int(stack.pop())