class Solution:
    def decodeString(self, s: str) -> str:
        result = ""
        stack = []
        curr = ""
        i=0
        while i != len(s):
            char = s[i]
            if char.isdigit():
                start=""
                while s[i].isdigit():
                    start += s[i]
                    i += 1
                stack.append((curr, start))
            else:
                if char == '[':
                    curr=""
                elif char == ']':
                    prev = stack[-1][0]
                    num = stack[-1][1]
                    curr = prev + (int(num) * curr)
                    stack.pop()
                else:
                    curr += char

                i+=1
            print(stack, curr)


        return curr
                                
                
                