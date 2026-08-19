class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        #case 1:
            #left and right are equal to each other. recurse left, right
        #case 2:
            #center and right are equal. recurse center left, right right
            #center and left are equal. recurse left left, center right
        substring = s[0]
        best_len = 1

        def dfs(l, r):
            nonlocal best_len
            nonlocal substring
            if l < 0 or r >= len(s):
                return

            if s[l] == s[r]:
                if r-l+1 > best_len:
                    substring = s[l:r+1]
                    best_len = r-l+1
                
                #odd
                dfs(l-1, r+1)


        for i in range(len(s)-1):
            dfs(i, i)
            dfs(i, i + 1) #even case
        
        return substring
