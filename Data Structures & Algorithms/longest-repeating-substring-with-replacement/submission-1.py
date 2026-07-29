class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        length = l = max_freq = 0
        m = {}
        for r in range(len(s)):
            m[s[r]] = m.get(s[r], 0) + 1
            max_freq = max(max_freq, m[s[r]])

            while r - l - max_freq > k - 1:
                m[s[l]] -= 1
                l += 1
            
            length = max(length, r - l + 1)

        return length

            
