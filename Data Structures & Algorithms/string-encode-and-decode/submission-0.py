class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        result = ""
        for s in strs:
            for char in s:
                result += str(ord(char))
                result += "#"
            result += "."
        print(result)
        return result

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        result = []
        slider = 0
        x = ""
        
        for i in range(len(s)):
            
            if s[i] == '.':
                result.append(x)
                slider += 1
                x = ""
            if s[i] == '#':
                x += chr(int(s[slider:i]))
                print(s[slider:i])
                slider = i + 1

            print(result)
        return result
            

