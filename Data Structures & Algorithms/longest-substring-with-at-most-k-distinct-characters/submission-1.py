class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        l = length = 0
        m = {}

        for i in range(len(s)):
            m[s[i]] = m.get(s[i], 0) + 1
            while len(m) > k:
                m[s[l]] -= 1
                if m[s[l]] == 0:
                    del m[s[l]]
                l += 1

            length = max(length, 1 + i - l)

        return length