class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        while l <= r:
            mid = (l+r)//2
            time = self.time_to_eat(piles, mid) 
            if time > h:
                l = mid + 1
                
            elif time <= h:
                r = mid - 1
            


        return l
                
                

    def time_to_eat(self, piles, k):
        time = 0
        for pile in piles:
            time += -(pile // -k) # floor rounds to negative infinity
        return time