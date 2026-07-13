class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        stack=[]
        operator='+'
        i=0
        while i < len(s):
            if not s[i].isdigit():
                operator = s[i]
                i+=1
            else:
                j=i
                while i < len(s) and s[i].isdigit():
                    i += 1
                num=int(s[j:i])
                if operator == '+':
                    stack.append(int(num))
                elif operator == '-':
                    stack.append(-int(num))
                elif operator == '*':
                    stack.append(stack.pop()*int(num))
                elif operator == '/':
                    #negative floor issue
                    stack.append(int(stack.pop()/int(num)))
            
        return sum(stack)