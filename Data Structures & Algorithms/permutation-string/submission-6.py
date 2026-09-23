class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        chars = {}
        charset = set()
        for c in s1: 
            chars[c] = chars.get(c, 0) + 1
            charset.add(c)

        l = numOfZeros=0
        for r in range(len(s2)):
            if s2[r] in charset:
                chars[s2[r]] -= 1
                if chars[s2[r]] == 0: numOfZeros += 1

                #if negative, jump until no longer negative
                while chars[s2[r]] < 0:
                    if chars[s2[l]] == 0: numOfZeros -= 1
                    chars[s2[l]] += 1
                    l += 1
                
            else: #jump window to R
                if s2[l] not in charset: l += 1
                else:
                    print(s2[l])    
                    while l < r:
                        if chars[s2[l]] == 0: numOfZeros -= 1
                        chars[s2[l]] += 1
                        l += 1
                    l += 1


            if numOfZeros == len(charset): return True
        return False