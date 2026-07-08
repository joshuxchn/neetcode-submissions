class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        stack.append(tokens[0])
        result = 0
        if len(tokens)==1:
            return int(tokens[0])
        for token in tokens[1:]:
            print(stack)
            if token == "+":
                a = stack.pop()
                b = stack.pop()
                result = int(b) + int(a)
                stack.append(result)
            elif token == "-":
                a = stack.pop()
                b = stack.pop()
                result = int(b) - int(a)
                stack.append(result)
            elif token == "/":
                a = stack.pop()
                b = stack.pop()
                result = int(b) / int(a)
                stack.append(result)
            elif token == "*":
                a = stack.pop()
                b = stack.pop()
                result = int(b) * int(a)
                stack.append(result)
            else:
                stack.append(token)
            print(result)
        return int(result)