class Solution:
    def rob(self, nums: List[int]) -> int:
        #bottom up
        if len(nums) == 1: return nums[0]
        cache = {}
        cache[0] = nums[0]
        cache[1] = max(nums[1], nums[0])

        for i in range(2, len(nums)):
            #max of the two previous plus this, or last one and skip this
            cache[i] = max(cache[i-2] + nums[i], cache[i-1])
        
        return cache[len(nums)-1]