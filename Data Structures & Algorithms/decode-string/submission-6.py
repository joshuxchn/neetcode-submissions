class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            
            if s[i] != ']':
                stack.append(s[i])
            else:
                result = "" #tracks chars inside bracket
                while stack[-1] != '[':
                    result = stack.pop() + result
                    
                stack.pop()

                #for multidigit char
                multiplier = ""
                while stack and stack[-1].isdigit():
                    multiplier = stack.pop() + multiplier

                stack.append(result * int(multiplier))
            
        return "".join(stack)
                                
                
                