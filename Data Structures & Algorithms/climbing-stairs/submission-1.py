class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * n #stores how many unique ways at that level
        def climb(i):
            if i >= n:
                return i == n
            if cache[i] != -1:
                return cache[i]
            cache[i] = climb(i + 1) + climb(i + 2)
            return cache[i]
        
        return climb(0)