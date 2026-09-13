class Solution:
    def tribonacci(self, n: int) -> int:
        cache = {}
        cache[0] = 0
        cache[1] = 1
        cache[2] = 1

        def dp(i):
            if i in cache: return cache[i]

            cache[i] = dp(i-1) + dp(i-2) + dp(i-3)
            return cache[i]

        return dp(n)