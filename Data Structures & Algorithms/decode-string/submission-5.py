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
                    multiplier = stack.pop() + multiplier

                stack.append(result * int(multiplier))
            print(stack)
            
        return "".join(stack)
                                
                
                