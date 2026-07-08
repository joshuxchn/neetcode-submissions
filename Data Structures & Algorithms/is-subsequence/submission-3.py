class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        x = 0
        if len(s) == 0:
            return True
        
        for char in t:
            if char==s[x]:
                x += 1
            if x == len(s):
                return True
        

        return False


#n...o....d..e..