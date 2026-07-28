class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        l = 0
        length = 0
        for i in range(len(s)):
            if s[i] in chars:
                length = max(length, i - l)
                
                while s[i] in chars:
                    chars.remove(s[l])
                    l += 1 
            chars.add(s[i])
        return max(length, len(chars))
