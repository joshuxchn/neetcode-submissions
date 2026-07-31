class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        for i in range(len(grumpy)):
            if grumpy[i]:
                grumpy[i] *= customers[i]

        l = 0
        count = sum(customers)
        max_saved = 0
        saved = 0

        for r in range(len(grumpy)):
            count -= grumpy[r]

            if r - l + 1 > minutes:
                saved -= grumpy[l]
                l += 1
            
            saved += grumpy[r]
            max_saved = max(saved, max_saved)
        




        return count + max_saved
                

            
            
            





#[2,(11),5,0,7]