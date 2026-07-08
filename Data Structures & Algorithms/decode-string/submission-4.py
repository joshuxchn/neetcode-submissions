class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            
            if s[i] != ']':
                stack.append(s[i])
            else:
                result = ""
                while stack[-1] != '[':
                    result = stack.pop() + result
                    
                stack.pop()

                multiplier = ""
                while stack and stack[-1].isdigit():
                    multiplier = stack[-1] + multiplier
                    stack.pop()
                result = result * int(multiplier)

                stack.append(result)
            print(stack)
            
        return "".join(stack)
                                
                
                