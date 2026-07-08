class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        map_ = {}
        for char in s:
            map_[char] = map_.get(char, 0) + 1
        

        only_odd = False
        for value in map_.values():
            if value % 2 != 0:
                if only_odd:
                    return False
                only_odd=True
        
        return True