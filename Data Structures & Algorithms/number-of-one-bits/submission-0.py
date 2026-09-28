class Solution:
    def hammingWeight(self, n: int) -> int:
        tally = 0
        while n != 0:
            if n % 2 != 0: tally += 1
            n = n // 2 
        return tally