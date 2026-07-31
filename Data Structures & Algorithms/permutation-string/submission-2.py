class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        chars = {}
        for c in s1:
            chars[c] = chars.get(c, 0) + 1
        
        l = 0
        num_of_zeros = len(chars)

        for r in range(len(s2)):
            if s2[r] in chars:
                chars[s2[r]] -= 1

                if chars[s2[r]] == 0:
                    num_of_zeros -= 1

                while chars[s2[r]] < 0:
                    if s2[l] in chars:
                        if chars[s2[l]] == 0:
                            num_of_zeros += 1
                        chars[s2[l]] += 1
                
                    l += 1

            while s2[r] not in chars and l < r:
                print(l)
                if s2[l] in chars:
                    if chars[s2[l]] == 0:
                        num_of_zeros += 1
                    chars[s2[l]] += 1
                l += 1
    
            if num_of_zeros == 0:
                return True  

            print(num_of_zeros, s2[r], chars)
        return False
            


            