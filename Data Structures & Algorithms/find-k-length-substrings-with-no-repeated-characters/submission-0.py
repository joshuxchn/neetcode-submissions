class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        l = 0
        chars = set()
        if k > len(s):
            return 0
        
        res = 0
        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])

            if r - l == k:
                if s[l] in chars:
                    chars.remove(s[l])
                l += 1

            if len(chars) == k:
                res += 1
    
            print(s[l:r+1], chars, res)
        
        return res

