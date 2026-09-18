class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] != ']': stack.append(s[i])
            else: 
                temp = ""
                while stack and stack[-1] != '[':
                    temp = stack.pop() + temp

                stack.pop() #pop left bracket
                nums = ""
                while stack and stack[-1].isdigit():
                    nums = stack.pop() + nums

                stack.append(temp * int(nums))
            print(stack)
        return "".join(stack)
                

                
                
                
