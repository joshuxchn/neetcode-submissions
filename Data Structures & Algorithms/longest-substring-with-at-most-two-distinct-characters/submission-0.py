class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        l = length = 0
        m = {}

        for i in range(len(s)):
            m[s[i]] = m.get(s[i], 0) + 1
            while len(m) > 2:
                m[s[l]] -= 1
                if m[s[l]] == 0:
                    del m[s[l]]
                l += 1

            length = max(length, 1 + i - l)

        return length