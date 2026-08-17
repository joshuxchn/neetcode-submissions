class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * n #stores how many unique ways at that level
        def climb(i):
            if i >= n:
                return i == n #returns 1 if true
            if cache[i] != -1: #if it already exist, don't calculate again
                return cache[i]
            cache[i] = climb(i + 1) + climb(i + 2)
            print(i, cache)
            return cache[i]
        
        return climb(0)