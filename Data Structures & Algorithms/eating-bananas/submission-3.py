class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def time(k):
            t = 0
            for p in piles:
                t += -(-p // k)
            return t <= h
        l=1
        r = max(piles)
        
        while l <= r:
            mid = (l+r)//2
            doable = time(mid)
            if doable:
                r = mid - 1
            else:
                l = mid + 1
        
        return l

