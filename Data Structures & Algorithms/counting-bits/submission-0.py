class Solution:
    def countBits(self, n: int) -> List[int]:

        def hammingWeight(n: int) -> int:
            tally = 0
            while n != 0:
                if n % 2 != 0: tally += 1
                n = n // 2 
            return tally

        tally = [0] * (n+1)
        
        for i in range(n+1):
            tally[i] = hammingWeight(i)
        return tally