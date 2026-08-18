class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * n
        def climb(i):
            if i > n:
                return 0
            if i == n: 
                return 1
            
            if cache[i] != -1: return cache[i]
            cache[i] = climb(i + 1) + climb(i+2)
            return cache[i]

        return climb(0)