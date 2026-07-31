class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        k = 1


        l = length = tally = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                tally += 1
                
            while tally > k:
                if nums[l] == 0:
                    tally -= 1
                l += 1
            
            length = max(length, r - l + 1)
        return length


