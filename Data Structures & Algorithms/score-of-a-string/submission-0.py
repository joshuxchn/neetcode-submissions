class Solution:
    def scoreOfString(self, s: str) -> int:
        sum=0
        for i in range(0, len(s)-1):
            if s[i+1]:
                sum += abs(ord(s[i]) - ord(s[i+1]))
            else:
                print("branch taken")
                sum += abs(ord(s[i]))
        
        return sum