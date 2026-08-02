class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = s = 0
        length = len(nums) + 1

        for r in range(len(nums)):
            s += nums[r]

            while s - nums[l] >= target: 
                #cool trick to not have to write another two lines
                # to compensate for being just under target
                s -= nums[l]
                l += 1
        
            if s >= target:
                length = min(length, r - l + 1)
        if length == len(nums) + 1:
            return 0
        return length
