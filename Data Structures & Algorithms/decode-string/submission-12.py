class Solution:
    def decodeString(self, s: str) -> str:
       #3
       #temp: a
       #closing bracket = pop, trigger
       #temp = aaa


       #3, 2
       #a, c
       #temp: acc acc ac
       
       #3[a2[bc]d]
       
        nums = []
        chars = []

        i = 0
        while i < len(s):
            if s[i].isdigit():
                temp = ""
                while s[i].isdigit():
                    temp += s[i]
                    i += 1
                nums.append(int(temp))
                chars.append("")
                continue
                
            elif s[i] != '[' and s[i] != ']':
                temp = ""
                while i < len(s) and s[i] != '[' and s[i] != ']' and not s[i].isdigit(): 
                    temp += s[i]
                    i += 1
                if len(chars) == 0: chars.append(temp)
                else: chars[-1] += temp
                continue

            if s[i] == ']':
                temp = nums.pop() * chars.pop()
                if len(chars) == 0: chars.append("")
                chars[-1] += temp
            
            i += 1
            print(chars, nums)
        return "".join(chars)

                
