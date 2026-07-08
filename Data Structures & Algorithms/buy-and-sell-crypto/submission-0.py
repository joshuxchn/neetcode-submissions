class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minval = 100000

        for i in prices:
            if i - minval > maxP:
                maxP = i - minval
            if i < minval:
                minval = i
    
    
        return maxP