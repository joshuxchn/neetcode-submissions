class Solution:
    def parseTernary(self, expression: str) -> str:
        stack=[]
        true_condition=""
        false_condition=""
        expression = expression[::-1]
        i=0
        while i != len(expression):
            if expression[i] != '?':
                stack.append(expression[i])
            else:
                true_condition = stack.pop()
                stack.pop()
                false_condition = stack.pop()
                i+=1
                if expression[i] == 'T':
                    stack.append(true_condition)
                else:
                    stack.append(false_condition)
            i += 1
        return "".join(stack)