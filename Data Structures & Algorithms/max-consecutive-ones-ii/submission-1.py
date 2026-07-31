class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        k = 1


        l = length = tally = 0 #how many 0's flipped

        for r in range(len(nums)):
            if nums[r] == 0: #flip another 0
                tally += 1
                
            while tally > k: #if flipped to many, jump to after last flipped 0. 
                             # Now you flipped K, which is valid
                if nums[l] == 0:
                    tally -= 1
                l += 1
            
            length = max(length, r - l + 1)
        return length


